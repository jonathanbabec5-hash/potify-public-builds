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
