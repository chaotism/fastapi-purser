TEST_PATH=./application/tests

init:
	pip install poetry
	poetry install

pre-commit:
	pre-commit install

black:
	black application/

test:
	export API_TEST=1
	export PYTHONPATH="`pwd`:$PYTHONPATH"
	poetry run python -m pytest --cov=app --verbose --color=yes $(TEST_PATH)
