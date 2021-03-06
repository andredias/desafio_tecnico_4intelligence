POSTGRESQL_RUNNING = $(shell docker ps | grep postgres-development)

run: start_postgres
	@ trap 'echo "Stopping postgres..."; docker stop postgres-development' INT; \
	ENV=development hypercorn --reload --config=hypercorn.toml 'app.main:app'


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


start_postgres:
	@ if [ -z "$(POSTGRESQL_RUNNING)" ]; then \
		echo 'Starting PostgreSQL...'; \
		docker run -d --rm -p 5432:5432 -e POSTGRES_DB=4intelligence \
			-e POSTGRES_PASSWORD=development_1234 --name postgres-development \
			postgres:alpine; \
	fi


run_in_docker:
	docker-compose up
