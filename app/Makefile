.PHONY: fmt install install-dev lint test

fmt:
	black . $(ARGS) --target-version py310

install:
	pip3 install --user -r requirements.txt

install-dev:
	pip3 install --user -r requirements_dev.txt

lint:
	flake8 .

test:
	coverage run -m pytest -s -vv tests &&\
	coverage report -m

lint-ci:
	flake8 .

fmt-ci:
	black --check . --target-version py310

run:
	python main.py