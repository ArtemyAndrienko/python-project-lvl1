brain-games:
	poetry run brain-games

install:
	poetry install

build:
	poetry build

publish-dry:
	poetry publish --dry-run

publish:
	poetry publish -r testpypi

lint:
	poetry run flake8 brain_games

package-install:
	python -m pip install dist/*.whl

.PHONY: install lint build publish