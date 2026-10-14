#!/usr/bin/make

CDIR := $(shell pwd)
export PYTHONPATH := $(CDIR):$(PYTHONPATH)

all: lint test

lint:
	pycodestyle hdltools
	pylint -s n --disable=import-error hdltools
	git diff --check --cached

test:
	python3 hdltools/apps/genstub.py -h
	python3 hdltools/apps/genwrap.py -h
	python3 hdltools/apps/modcomp.py -h
	python3 hdltools/apps/modjson.py -h

clean:
	py3clean .
	rm -fr .pytest_cache
	rm -fr `find . -name __pycache__`
