# FastAPI REST API / Microservice (Python 3.10)

A small, production-shaped FastAPI service with versioned CRUD endpoints,
validation, centralized configuration, automated tests, Docker support, and
tool-trigger fixtures adapted from
[`testable-platform/Golden_Repo_Lite`](https://github.com/testable-platform/Golden_Repo_Lite/tree/python/Python_3.10).

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Open `http://localhost:8000/docs` for Swagger UI or call:

```bash
curl http://localhost:8000/health
curl -X POST http://localhost:8000/api/v1/items \
  -H "Content-Type: application/json" \
  -d '{"name":"Keyboard","price":99.5}'
```

## API

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/health` | Liveness check |
| `GET` | `/api/v1/items` | List items with `offset` and `limit` |
| `POST` | `/api/v1/items` | Create an item |
| `GET` | `/api/v1/items/{id}` | Fetch an item |
| `PATCH` | `/api/v1/items/{id}` | Partially update an item |
| `DELETE` | `/api/v1/items/{id}` | Delete an item |

The default store is intentionally in memory. `ItemService` provides a clean
boundary for replacing it with a database repository.

## Quality checks

```bash
pytest
pytest --cov=app --cov-branch --cov-report=term-missing
ruff check app tests
docker compose up --build
```

## Tool triggers

`tool-triggers/` contains the Python 3.10 fixtures and `trigger.yaml` metadata
from the Golden Repo reference. Some fixtures intentionally contain vulnerable,
complex, or lint-invalid code so their named analysis tool has a genuine finding.
They are isolated from the service package and normal test discovery.

Run a trigger from its directory, for example:

```bash
cd tool-triggers/coverage-py
bash run_coverage.sh
```

Each directory README lists its required tool and expected result. Security
fixtures must never be imported into application code or shipped as runtime code.

## Layout

```text
app/
  api/routes/       HTTP endpoints
  core/             configuration and logging
  schemas/          Pydantic request/response models
  services/         business logic and storage boundary
tests/              FastAPI integration tests
tool-triggers/      isolated tool-detection fixtures and metadata
```
