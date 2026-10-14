#!/usr/bin/make

all: lint test

lint:
	pycodestyle hdltools
	pylint -s n --disable=import-error hdltools
	git diff --check --cached

test:
	genstub -h && genwrap -h && modcomp -h && modjson -h

clean:
	py3clean .
	rm -fr .pytest_cache
	rm -fr `find . -name __pycache__`
