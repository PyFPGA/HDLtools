#!/usr/bin/make

all: lint test

lint:
	pycodestyle hdltools tests
	pylint -s n hdltools
	git diff --check --cached

test:
	PYTHONPATH=$(PWD) pytest -vv

clean:
	py3clean .
	rm -fr .pytest_cache
	rm -fr `find . -name __pycache__`
