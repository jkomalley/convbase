# Justfile

# Default task
default: all

# Install development dependencies
setup:
    uv pip install -e .[dev]

# Lint and format the codebase
lint:
    uv run ruff check --fix .
    uv run ruff format .

# Run tests with coverage
test:
    uv run pytest --cov=src/convbase --cov-branch -q

# Run type checker
type:
    uv run ty check --error-on-warning

# Run all checks
all: lint type test
