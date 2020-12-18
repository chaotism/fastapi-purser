APP_PATH=./application
TEST_PATH=./tests

init:
	pip install poetry
	poetry install

pre-commit:
	pre-commit install

black:
	black application/

test:
	cd $(APP_PATH) && poetry run python -m pytest --cov=application --verbose --color=yes $(TEST_PATH)
