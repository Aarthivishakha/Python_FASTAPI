# Integrated tool triggers (Python 3.16)

This directory contains all 14 trigger configurations found across the Python
branch of `testable-platform/Golden_Repo_Lite`. Unlike the original standalone
fixtures, these manifests analyze this FastAPI repository directly.

| # | Trigger | Tool(s) | Project input | Purpose |
|---:|---|---|---|---|
| 1 | `beniget` | Beniget | `app/` | Def-use/data-flow analysis |
| 2 | `cognitive-ast` | complexipy | `app/` | Cognitive complexity |
| 3 | `cosmic-ray` | Cosmic Ray | service + tests | Mutation testing |
| 4 | `coverage-py` | coverage.py | `app/` + `tests/` | Branch/statement coverage |
| 5 | `coverage-py-beniget` | coverage.py + Beniget | `app/` + `tests/` | Coverage plus data flow |
| 6 | `crosshair` | CrossHair | `app/` | Symbolic path/contract analysis |
| 7 | `jscpd` | jscpd | `app/` + `tests/` | Duplicate-code detection |
| 8 | `pip-audit` | pip-audit | `requirements*.txt` | Dependency vulnerabilities |
| 9 | `pydriller` | PyDriller | Git history | Code churn |
| 10 | `pylint` | pylint | `app/` + `tests/` | Static lint analysis |
| 11 | `pymcdc` | pymcdc | routes + tests | Condition coverage |
| 12 | `radon-lizard` | radon + lizard | `app/` | Cyclomatic complexity |
| 13 | `semgrep-bandit` | Semgrep + Bandit | `app/` | Security SAST |
| 14 | `testmon` | pytest-testmon | `app/` + `tests/` | Selective test execution |

Every directory contains a `trigger.yaml` with the command, versions,
requirements, expected result, and repository-relative target paths. Run commands
from the repository root. Install optional tool dependencies with:

```bash
python -m pip install -r tool-triggers/requirements.txt
```

`jscpd` additionally requires Node.js/npm. Tool dependencies are intentionally
separate from runtime dependencies so none are shipped with the API.
