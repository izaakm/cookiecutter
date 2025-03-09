USE_SSH := true

.PHONY: init install

install:
	pip install --editable .

init: | .git
.git:
	git init
	git add -A
	git commit -m "Initial commit"
	git branch -M main
ifeq ($(USE_SSH), true)
	git remote add origin git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git
else
	git remote add origin https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git
endif
	git push -u origin main
	@echo "push with: git push -u origin main"
