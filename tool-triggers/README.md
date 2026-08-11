# Python 3.10 tool-trigger fixtures

These isolated fixtures mirror `Golden_Repo_Lite/Python_3.10`. Each directory
contains a `trigger.yaml`, a runner, a short explanation, and the smallest source
or test files needed to make the named tool produce a real result.

| Directory | Tooling | Expected trigger |
|---|---|---|
| `cognitive-ast` | complexipy | High cognitive complexity |
| `cosmic-ray` | cosmic-ray | Mutants generated and tested |
| `coverage-py` | coverage.py | Statement and branch report |
| `coverage-py-beniget` | coverage.py + Beniget | Coverage and a dead definition |
| `pip-audit` | pip-audit | Known dependency CVEs |
| `pylint` | pylint | Lint violations |
| `pymcdc` | pymcdc | MC/DC conditions covered |
| `radon-lizard` | radon + lizard | Cyclomatic complexity above one |
| `semgrep-bandit` | Semgrep + Bandit | Intentional SAST findings |
| `testmon` | pytest-testmon | Selective rerun data recorded |

Install and run tools only in an isolated development environment. In particular,
the vulnerable packages and insecure code under `pip-audit` and `semgrep-bandit`
are test fixtures, not application dependencies.
