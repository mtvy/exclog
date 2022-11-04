VERSION=0.0.1

all: build check upload

build:
	python3 -m build

check:
	twine check dist/*

upload:
	twine upload dist/exclog-$(VERSION).tar.gz dist/exclog-$(VERSION)-py3-none-any.whl
