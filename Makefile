install:
	pip3 install -r requirements.txt

format:
	black src/*.py
	black test/*.py

test_file:
	pytest -vv --nbval -cov=my_lib -cov=main test/test_*.py *.ipynb

lint:
	ruff check src/*.py
	ruff check test/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < .devcontainer/Dockerfile

all: install format lint container-lint test 

generate_and_push: 
	python src/main.py
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add . ;\
		git commit -m"Add generated plot and report"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi