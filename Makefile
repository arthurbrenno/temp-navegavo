.PHONY: run

.DEFAULT_GOAL := run

run:
	clear
	@echo "Running..."
	uv run python -m navegavo

b:
	uvx ruff format navegavo

dbuild:
	clear
	@echo "Building..."
	docker build --pull --rm -f "Dockerfile" -t navegavo:latest "." 

drun:
	clear
	@echo "Running..."
	docker run -it --rm --name navegavo navegavo:latest

sync:
	clear
	uv sync


push:
	bash scripts/push.sh
