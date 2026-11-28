import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from verify import validate


class CatalogTest(unittest.TestCase):
    def test_catalog_validates(self):
        validate(json.loads((ROOT / "data/projects.json").read_text()))

    def test_duplicate_repository_is_rejected(self):
        row = {"repository":"Potify", "commit":"a"*40, "tree":"b"*40, "branch":"main", "purpose":"game", "scope":"source"}
        with self.assertRaises(ValueError):
            validate([row, dict(row, repository="potify")])

    def test_incomplete_commit_is_rejected(self):
        with self.assertRaises(ValueError):
            validate([{"repository":"demo", "commit":"deadbeef"}])


class ProjectIndexTest(unittest.TestCase):
    def test_index_lists_each_project_once(self):
        import re
        projects = json.loads((ROOT / "data/projects.json").read_text())
        index = (ROOT / "docs/PROJECT-INDEX.md").read_text()
        found = re.findall(r"\]\(https://github\.com/jonathanbabec5-hash/([A-Za-z0-9_.-]+)\)", index)
        expected = [row["repository"].casefold() for row in projects]
        self.assertEqual(len(found), len(expected))
        self.assertEqual(set(name.casefold() for name in found), set(expected))
        self.assertEqual(len(set(name.casefold() for name in found)), len(found))


class RemoteVerificationTest(unittest.TestCase):
    def setUp(self):
        self.row = {"repository": "demo", "commit": "a" * 40, "tree": "b" * 40, "branch": "main"}
        self.info = {"owner": {"login": "jonathanbabec5-hash"}, "visibility": "public"}
        self.commit = {"sha": "a" * 40, "commit": {"tree": {"sha": "b" * 40}}}

    def test_current_branch_is_verified(self):
        from unittest.mock import patch
        from verify import verify_remote
        branch = {"commit": {"sha": "a" * 40}}
        with patch("verify.api", side_effect=[self.info, self.commit, branch]):
            self.assertEqual(verify_remote(self.row), "demo")

    def test_snapshot_accepts_a_historical_commit_without_branch_query(self):
        from unittest.mock import patch
        from verify import verify_remote
        with patch("verify.api", side_effect=[self.info, self.commit]) as api:
            self.assertEqual(verify_remote(self.row, require_current=False), "demo")
            self.assertEqual(api.call_count, 2)

    def test_strict_remote_rejects_branch_drift(self):
        from unittest.mock import patch
        from verify import verify_remote
        with patch("verify.api", side_effect=[self.info, self.commit, {"commit": {"sha": "c" * 40}}]):
            with self.assertRaisesRegex(ValueError, "Branch has changed"):
                verify_remote(self.row)

    def test_rejects_snapshot_tree_mismatch(self):
        from unittest.mock import patch
        from verify import verify_remote
        wrong = {"sha": "a" * 40, "commit": {"tree": {"sha": "c" * 40}}}
        with patch("verify.api", side_effect=[self.info, wrong]):
            with self.assertRaisesRegex(ValueError, "commit or tree mismatch"):
                verify_remote(self.row, require_current=False)

    def test_rejects_private_repository(self):
        from unittest.mock import patch
        from verify import verify_remote
        with patch("verify.api", return_value={"owner": {"login": "jonathanbabec5-hash"}, "visibility": "private"}):
            with self.assertRaisesRegex(ValueError, "visibility mismatch"):
                verify_remote(self.row, require_current=False)
