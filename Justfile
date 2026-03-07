# Justfile

# Default task
default: all

# Install development dependencies
setup:
    uv sync

# Lint and format the codebase
lint:
    uv run ruff check --fix .
    uv run ruff format .

# Run tests with coverage
test:
    uv run pytest -q

# Run type checker
type:
    uv run ty check --error-on-warning

# Run all checks
all: lint type test
