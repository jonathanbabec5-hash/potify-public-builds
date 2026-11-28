"""Validate the catalog and optionally reconcile owner, visibility, branch and tree with GitHub."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
OWNER = "jonathanbabec5-hash"


def validate(rows):
    names = set()
    for row in rows:
        repo = row["repository"]
        if not re.fullmatch(r"[A-Za-z0-9_.-]+", repo) or repo.casefold() in names:
            raise ValueError(f"Invalid or duplicate repository: {repo}")
        names.add(repo.casefold())
        for field in ("commit", "tree"):
            if not re.fullmatch(r"[a-f0-9]{40}", row[field]):
                raise ValueError(f"Invalid {field} for {repo}")
        if not row["branch"] or not row["purpose"] or not row["scope"]:
            raise ValueError(f"Incomplete entry for {repo}")
    if not rows:
        raise ValueError("Empty catalog")


def api(path):
    return json.loads(subprocess.check_output(["gh", "api", path], text=True))


def verify_remote(row, require_current=True):
    """Verify a pinned public snapshot; optionally require its branch to match."""
    repo = row["repository"]
    path = f"repos/{OWNER}/{repo}"
    info = api(path)
    if info["owner"]["login"].lower() != OWNER or info["visibility"] != "public":
        raise ValueError(f"Owner or visibility mismatch: {repo}")
    snapshot = api(path + "/commits/" + row["commit"])
    if snapshot["sha"] != row["commit"] or snapshot["commit"]["tree"]["sha"] != row["tree"]:
        raise ValueError(f"Recorded commit or tree mismatch: {repo}")
    if require_current:
        branch = api(path + "/branches/" + quote(row["branch"], safe=""))
        if branch["commit"]["sha"] != row["commit"]:
            raise ValueError(f"Branch has changed: {repo}. Review the new commit and refresh the catalog.")
    return repo


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--remote", action="store_true", help="Verify snapshots and require recorded branches to match using gh.")
    modes.add_argument("--snapshot", action="store_true", help="Verify pinned public commits and trees without requiring current branches to match using gh.")
    args = parser.parse_args()
    rows = json.loads((ROOT / "data/projects.json").read_text())
    validate(rows)
    if args.remote or args.snapshot:
        from functools import partial
        check = partial(verify_remote, require_current=args.remote)
        with ThreadPoolExecutor(max_workers=4) as pool:
            for name in pool.map(check, rows):
                print("Verified " + name, flush=True)
    print(f"{len(rows)} catalog entries validated.")
