.PHONY: clean install flake8

clean:
	@echo 'Cleaning .pyc and __pycache__ files'
	$(shell find * -name "*.pyc" -delete)
	$(shell find * -name "__pycache__" -delete)

install: clean
	pip install -r requirements.txt --allow-all-external

flake8: clean
	flake8 .

dist: flake8
	python setup.py sdist
