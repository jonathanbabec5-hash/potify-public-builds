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
