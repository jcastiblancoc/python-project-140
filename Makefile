install:
	uv pip install -e .

brain-games:
	brain-games

brain-even:
	brain-even

brain-calc:
	brain-calc

brain-gdc:
	brain-gcd

brain-progression:
	brain-progression

brain-prime:
	brain-prime

build:
	uv pip compile -o requirements.txt pyproject.toml
	uv pip sync requirements.txt

package-install:
	uv pip install dist/*.whl

lint:
	uv run ruff check brain_games --fix
