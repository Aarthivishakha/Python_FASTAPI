# pydriller — Python 3.9

A standalone python command (`catalog/mine_history.py`) that mines this
repo's own git history, which is pydriller's actual trigger source
(it reads git log directly; no fixture file needed).

Run from repo root:

```bash
python catalog/mine_history.py --max-commits 200
```
