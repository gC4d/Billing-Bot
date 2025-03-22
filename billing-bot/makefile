ifneq ("$(wildcard .env)","")
	include .env
	export
endif

test:
	pytest ./app/tests/unit -v

fmt:
	make -k ruff-fmt black-fmt

lint:
	make -k ruff-check black-check mypy-check

black-fmt:
	python -m black ./app

black-check:
	python -m black --check ./app

ruff-fmt:
	python -m ruff check --fix-only --unsafe-fixes ./app

ruff-check:
	python -m ruff check --fix-only --unsafe-fixes ./app

mypy-check:
	python -m mypy ./app
