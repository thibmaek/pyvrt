.PHONY: build

lint:
	black pyvrt/

install:
	python -m venv .
	source bin/activate
	python setup.py install
	pip install -r requirements.txt

build: lint
	rm -rf build/ dist/
	python setup.py sdist bdist_wheel

publish: build
	twine upload dist/*
