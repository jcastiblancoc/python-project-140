install:
	uv pip install -e .

brain-games:
	brain-games

brain-even:
	brain-even

build:
	uv pip compile -o requirements.txt pyproject.toml
	uv pip sync requirements.txt

package-install:
	uv pip install dist/*.whl

lint:
	uv run ruff check brain_games --fix
