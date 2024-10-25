.PHONY: init install lint test format

init:
	git init
	git add -A
	git commit -m "Initial commit"
	git branch -M main
	@echo "push with: git push -u origin main"

install:
	pip install --editable .

# lint:
# 	flake8
# 	black --check .

# test: lint
# 	pytest

# format:
# 	black .
