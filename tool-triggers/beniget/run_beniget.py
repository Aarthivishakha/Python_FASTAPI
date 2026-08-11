"""Generate a Beniget def-use summary for repository Python files."""
import json
import sys
from pathlib import Path
from typing import Dict

import gast as ast
from beniget import DefUseChains


def main() -> None:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "app")
    report: Dict[str, int] = {}
    for path in sorted(root.rglob("*.py")):
        module = ast.parse(path.read_text(encoding="utf-8"))
        chains = DefUseChains(filename=str(path))
        chains.visit(module)
        report[path.as_posix()] = len(chains.chains)
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
