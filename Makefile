.PHONY: build

lint: venv
	black pyvrt/

venv:
	python -m venv .
	source bin/activate

install: venv
	python setup.py install
	pip install -r requirements.txt

build: venv
	rm -rf build/ dist/
	python setup.py sdist bdist_wheel

publish: lint build
	twine upload dist/*

