all: clean test

test:
	tox	

clean-pyc:
	find . -name \*.pyc -delete
	find . -name \*.pyo -delete
	find . -name \*~ -delete

clean: clean-pyc
	rm -rf build dist nosetests.xml cover .coverage *.egg-info
