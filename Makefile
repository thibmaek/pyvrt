.PHONY: build

install:
	python3 setup.py install

build:
	rm -rf build/ dist/
	python3 setup.py sdist bdist_wheel
