.PHONY: install run test coverage lint docker-build docker-run

install:
	python -m pip install -r requirements-dev.txt

run:
	uvicorn app.main:app --reload

test:
	pytest

coverage:
	pytest --cov=app --cov-branch --cov-report=term-missing

lint:
	flake8 app tests

docker-build:
	docker build -t fastapi-microservice .

docker-run:
	docker run --rm -p 8000:8000 fastapi-microservice
