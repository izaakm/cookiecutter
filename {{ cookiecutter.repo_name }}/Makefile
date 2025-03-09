.PHONY: init install

install:
	pip install --editable .

init: | .git
	git init
	git add -A
	git commit -m "Initial commit"
	git branch -M main
	@echo "push with: git push -u origin main"
