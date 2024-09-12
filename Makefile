.PHONY: run

.DEFAULT_GOAL := run

run:
	@echo "Running..."
	uv run python -m navegavo


push:
	bash scripts/push.sh
