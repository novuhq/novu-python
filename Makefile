# This file is covered by the LICENSE file in the root of this project.

# Environment variables

SHELL = /bin/bash

CURRENT_USER := $(shell whoami)
CURRENT_UID := $(shell id -u)
CURRENT_GID := $(shell id -g)

export CURRENT_USER
export CURRENT_UID
export CURRENT_GID

# Commands

default: help

.PHONY: python-install
python-install: ## Installs Python environment.
	poetry install

.PHONY: check-lint
check-lint: ## Runs linters.
	.venv/bin/pylama

.PHONY: check-security
check-security: ## Runs security checks.
	.venv/bin/bandit -r intranet

.PHONY: tests
tests: ## Runs tests with coverage.
	.venv/bin/coverage erase; exit 0
	.venv/bin/coverage run; exit 0
	.venv/bin/coverage html; exit 0
	.venv/bin/coverage xml; exit 0
	.venv/bin/coverage report -m

.PHONY: precommit
precommit: ## Runs pre-commit.
	.venv/bin/pre-commit run --all-files

.PHONY: docs
docs: ## Builds documentation.
	.venv/bin/sphinx-build -b html docs public

.PHONY: help
help: ## Lists all the available commands.
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
