 # we want bash behaviour in all shell invocations
SHELL := bash
# Run each target in a separate shell
.ONESHELL:
 # Fail on error inside any functions or subshells
.SHELLFLAGS := -eu -o pipefail -c
 # Remove partially created files on error
.DELETE_ON_ERROR:
 # Warn when an undefined variable is referenced
MAKEFLAGS += --warn-undefined-variables
# Disable built-in rules
MAKEFLAGS += --no-builtin-rules


help: # Show this help
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  help               Show this help"
	@echo "  clean              Clean unused files"
	@echo "  lint               Run linters"
	@echo "  test               Run tests"
	@echo "  start-dev          Start dev server"
	@echo "  migrate            Run migrations"
	@echo "  revision           Create a new migration"


.PHONY: lint
lint: # Run linters
	pre-commit run --all-files

.PHONY: test
test: # Run tests
	python -m pytest -vv -s --cov=app --cov-report=xml --cov-branch tests

.PHONY: start-dev
start-dev: # Run dev server
	./scripts/start_dev.sh

.PHONY: clean
clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build

.PHONY: migrate
migrate: # Run migrations
	python -m alembic upgrade heads

.PHONY: revision
revision: # Create a new migration
	python -m alembic revision --autogenerate -m "$(message)"