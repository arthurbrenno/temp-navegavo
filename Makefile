.PHONY: run

.DEFAULT_GOAL := run

run:
	clear
	@echo "Running..."
	uv run python -m navegavo

b:
	uvx ruff format navegavo

sync:
	clear
	uv sync


push:
	bash scripts/push.sh
