lint:
	@echo
	isort --diff -c --skip-glob '*.venv' .
	@echo
	blue --check --diff --color .
	@echo
	flake8 .
	@echo
	mypy .

format_code:
	isort .
	blue .

test_only:
	pytest -svx

test: lint test_only
