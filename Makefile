.PHONY: install run test coverage lint docker-up

install:
	python -m pip install -r requirements-dev.txt

run:
	uvicorn app.main:app --reload

test:
	pytest

coverage:
	pytest --cov=app --cov-branch --cov-report=term-missing

lint:
	ruff check app tests

docker-up:
	docker compose up --build
