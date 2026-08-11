"""Mines this project's own git commit history via pydriller and reports per-file churn."""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

from pydriller import Repository


def main():
    parser = argparse.ArgumentParser(description="Report per-file git churn for this project using pydriller.")
    parser.add_argument("--max-commits", type=int, default=200)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    churn: dict[str, dict[str, int]] = defaultdict(lambda: {"commits": 0, "added": 0, "removed": 0})
    commits_seen = 0

    for commit in Repository(str(root)).traverse_commits():
        commits_seen += 1
        for mod in commit.modified_files:
            path = mod.new_path or mod.old_path
            if not path:
                continue
            path = path.replace("\\", "/")
            churn[path]["commits"] += 1
            churn[path]["added"] += mod.added_lines
            churn[path]["removed"] += mod.deleted_lines
        if commits_seen >= args.max_commits:
            break

    top_churned = sorted(churn.items(), key=lambda kv: kv[1]["commits"], reverse=True)[:10]
    summary = {
        "commits_analyzed": commits_seen,
        "files_touched": len(churn),
        "top_churned_files": [{"path": p, **stats} for p, stats in top_churned],
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
