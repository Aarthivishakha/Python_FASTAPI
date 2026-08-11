.PHONY: install test build

install:
	pip install -r requirements.txt
	pip install -r quality/requirements.txt

test:
	pytest catalog/tests

build:
	bash build.sh
