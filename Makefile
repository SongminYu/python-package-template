build-wheel:
	python setup.py bdist_wheel

format:
	black .

lint:
	pylint --rcfile=.pylintrc package_name

test:
	pytest -s

test-cov:
	pytest -s --cov

