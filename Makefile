#!/usr/bin/make

all: lint test

lint:
	PYTHONPATH=$(PWD) pycodestyle hdltools tests
	PYTHONPATH=$(PWD) pylint -s n hdltools
	git diff --check --cached

test:
	PYTHONPATH=$(PWD) python3 hdltools/apps/genstub.py -h
	PYTHONPATH=$(PWD) python3 hdltools/apps/genwrap.py -h
	PYTHONPATH=$(PWD) python3 hdltools/apps/modcomp.py -h
	PYTHONPATH=$(PWD) python3 hdltools/apps/modjson.py -h

clean:
	py3clean .
	rm -fr .pytest_cache
	rm -fr `find . -name __pycache__`
