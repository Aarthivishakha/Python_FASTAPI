# semgrep + bandit — Python 3.9

Runs SAST against the real `catalog/` code, including the
intentionally hardcoded `API_SECRET_KEY` in `catalog/main.py`.

Run from repo root:

```bash
bandit -r catalog
semgrep --config auto catalog
```
