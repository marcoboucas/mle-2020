MODULE = content_based_filtering
lint:
	python -m pylint $(MODULE)
	python -m flake8 $(MODULE)
	python -m mypy $(MODULE)

test:
	python3 -m unittest discover -t . -s tests -v

tests: test

coverage:
	coverage run --source=topic_modeling -m unittest discover -t . -s tests -v
	coverage report -m