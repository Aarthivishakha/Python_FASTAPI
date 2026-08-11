# FastAPI REST API / Microservice (Python 3.14)

A small, production-shaped FastAPI service with versioned CRUD endpoints,
validation, centralized configuration, automated tests, optional Docker support,
and integrated tool triggers adapted from
[`testable-platform/Golden_Repo_Lite`](https://github.com/testable-platform/Golden_Repo_Lite/tree/python).

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
docker build -t fastapi-microservice .
docker run --rm -p 8000:8000 fastapi-microservice
```

## Tool triggers

`tool-triggers/` contains all 14 trigger configurations found across the Golden
Repo Python branch. The manifests are integrated with this repository: they
target `app/`, `tests/`, dependency files, or this repository's Git history.
Install the optional tools separately from runtime dependencies:

```bash
python -m pip install -r tool-triggers/requirements.txt
pytest --cov=app --cov-branch --cov-report=term-missing tests
```

See `tool-triggers/README.md` for the complete 14-tool matrix and commands.

## Why the Dockerfile exists

Docker is optional for local development. The `Dockerfile` pins the runtime to
Python 3.14, installs only production dependencies, runs as a non-root user, and
provides the same deployable environment on any machine or CI platform. Compose
was removed because this service currently has no database, queue, or second
container to orchestrate.

## Layout

```text
app/
  api/routes/       HTTP endpoints
  core/             configuration and logging
  schemas/          Pydantic request/response models
  services/         business logic and storage boundary
tests/              FastAPI integration tests
tool-triggers/      14 integrated analysis-tool manifests
```
