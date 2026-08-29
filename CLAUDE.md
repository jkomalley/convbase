# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`convbase` is a command-line utility for converting integers between binary, octal, decimal, and hexadecimal bases. Python 3.11+, src layout, managed with `uv`, published to PyPI as `convbase`.

It installs four console scripts — `bin`, `oct`, `dec`, `hex` — one per output base. There is no single umbrella command.

## Commands

- **Install deps:** `just install` (`uv sync` + `uv run pre-commit install`)
- **Run the CLI locally:** `just run hex 255` (`uv run hex 255`)
- **Run tests:** `just test` (`uv run pytest`)
- **Run single test:** `uv run pytest tests/test_lib.py::test_to_binary -v`
- **Test with coverage (100% gate):** `just test-cov` — an alias for `just test`; the
  coverage flags and the `--cov-fail-under=100` gate live in `[tool.pytest.ini_options]`
  `addopts`, so every `pytest` run is already gated.
- **Format:** `just format` (`uv run ruff format src/ tests/`)
- **Format check:** `just format-check` (`uv run ruff format --check src/ tests/`)
- **Lint (auto-fix):** `just lint` (`uv run ruff check --fix src/ tests/`)
- **Lint check:** `just lint-check` (`uv run ruff check src/ tests/`)
- **Type check:** `just typecheck` (`uv run ty check src/`)
- **Everything:** `just check` (format-check + lint-check + typecheck + test-cov)
- **Clean caches:** `just clean`
- **Upgrade lockfile:** `just lock-upgrade`
- **Bump version:** `just bump-version <major|minor|patch|dev|beta|alpha|rc>` (`uv version --bump <part>`)

## Architecture

The project uses a `src/convbase/` layout with this module structure:

- `lib.py` — The whole conversion layer: `to_binary`, `to_octal`, `to_decimal`,
  `to_hexadecimal`. Each takes a string and returns a string. All four parse with
  `int(value, 0)`, which is what gives every command the same accepted input set
  (bare decimal, or `0b`/`0o`/`0x`-prefixed) rather than four different ones.
  No click, no I/O, no error handling — a bad value raises `ValueError`.
- `cli.py` — Four `click.command()` entry points (`bin_cmd`, `oct_cmd`, `dec_cmd`,
  `hex_cmd`), one per console script. Each is a thin wrapper: call the matching
  `lib` function, `click.echo` the result, and translate `ValueError` into
  `click.BadParameter` so the failure reads as a CLI usage error rather than a
  traceback.
- `__init__.py` — Public API re-exports (the four `to_*` functions). The package is
  usable as a library, not only as a CLI.

Key design decisions:

- **`int(value, 0)` is the single parsing rule.** Base auto-detection from the
  prefix comes free from the stdlib; there is no hand-rolled prefix handling to
  keep in sync across the four commands.
- **`lib` never knows about click.** Conversion is pure and independently testable;
  presentation and exit codes live only in `cli.py`. Keep it that way when adding
  a base.
- **Errors surface as `click.BadParameter`, chained from the original
  `ValueError`** (`raise ... from err`). The user sees
  `Error: Invalid value for 'VALUE': invalid integer: 'hello'` and a non-zero exit.
- **`hex` output is lowercase** (`hex(255)` → `0xff`), matching Python's own
  formatting rather than normalizing case.

## Workflow

- Every feature, fix, or other change gets its own branch and pull request — no direct commits to main.
- Commits must be atomic and follow Conventional Commits (`feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `ci`, `deps`, `style`): one logical change per commit.
- PRs that resolve an issue reference it with `Closes #N` so it closes automatically on merge.
- **PRs are rebase-merged.** Squash and merge commits are disabled at the repo level, for bots and humans alike.
- **Keep `CHANGELOG.md` release-ready.** Any user-facing change adds a bullet under `## [Unreleased]` in the same PR (internal-only refactors, CI, test, and docs changes are exempt). Entries follow the existing Keep a Changelog style — grouped under `### Added`/`### Changed`/`### Fixed`/`### Removed`, one line each.
- **Releases are automated and notes come from the changelog — never hand-written commit dumps.** See CONTRIBUTING.md → Releasing.

## Code Style

- Google-style docstrings (enforced by ruff).
- Line length: 88 chars.
- Ruff `select = ["ALL"]` with a pragmatic, curated set of ignores (see `pyproject.toml`).
- Tests are exempt from docstring and type-annotation rules.
- Prefer comments that explain *why* code does something, not *what* it does.

## Testing Notes

- 100% branch coverage is a hard gate (`--cov-fail-under=100` in `addopts`) — every new branch needs a test, and CI runs plain `uv run pytest`, so the gate applies there too.
- `tests/test_lib.py` covers the pure conversion functions; `tests/test_cli.py` drives the click commands through `click.testing.CliRunner`.
- Both files are heavily parametrized. Ruff's `PT006` is enforced, so the first argument to `pytest.mark.parametrize` must be a **tuple** of names — `("value", "expected")`, not `"value, expected"`.
- `pytest.raises` must carry a `match=` (ruff `PT011`); the conversion failures match on `"invalid literal for int"`.
