.PHONY: build

lint:
	black pyvrt/

install:
	python3 -m venv .
	source bin/activate
	python setup.py install
	pip install -r requirements.txt

build: lint
	rm -rf build/ dist/
	python3 setup.py sdist bdist_wheel
