.PHONY: build

lint:
	bin/black pyvrt/

install:
	python -m venv .
	source bin/activate
	python setup.py install
	pip install -r requirements.txt

build:
	rm -rf build/ dist/
	bin/python setup.py sdist bdist_wheel

publish: lint build
	bin/twine upload dist/*
