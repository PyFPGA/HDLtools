#!/usr/bin/make

all: lint

lint:
	pycodestyle hdltools tests
	pylint -s n hdltools
	git diff --check --cached

clean:
	py3clean .
	rm -fr `find . -name __pycache__`
