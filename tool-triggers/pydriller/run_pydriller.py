"""Report file churn from this repository's real Git history."""
import json
from collections import defaultdict
from pathlib import Path

from pydriller import Repository


def main(max_commits: int = 200) -> None:
    root = Path(__file__).resolve().parents[2]
    churn: dict[str, dict[str, int]] = defaultdict(
        lambda: {"commits": 0, "added": 0, "removed": 0}
    )
    commits_seen = 0
    for commit in Repository(str(root)).traverse_commits():
        commits_seen += 1
        for change in commit.modified_files:
            path = change.new_path or change.old_path
            if path:
                churn[path]["commits"] += 1
                churn[path]["added"] += change.added_lines
                churn[path]["removed"] += change.deleted_lines
        if commits_seen >= max_commits:
            break
    print(json.dumps({"commits": commits_seen, "files": churn}, indent=2))


if __name__ == "__main__":
    main()
