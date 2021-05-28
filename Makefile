run:
	hypercorn --reload --config=hypercorn.toml 'app.main:app'


lint:
	@echo
	isort --diff -c --skip-glob '*.venv' .
	@echo
	blue --check --diff --color .
	@echo
	flake8 .
	@echo
	mypy --ignore-missing-imports .

format_code:
	isort .
	blue .

test_only:
	pytest -svx --cov-report term-missing --cov-report html --cov-branch \
			--cov app/

test: lint test_only
