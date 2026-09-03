# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-09-02

### Added

- The package now ships a `py.typed` marker and declares `Typing :: Typed`, so
  downstream type checkers see convbase's inline annotations instead of
  treating the package as untyped.
- Full type annotations on the CLI command functions.

### Changed

- CLI `--help` text reworded to imperative mood ("Convert VALUE to binary"
  rather than "Converts VALUE to binary") and reflowed. Behaviour is unchanged.
- `click.BadParameter` is now raised with `from err`, so tracebacks retain the
  underlying `ValueError` instead of discarding it.
- Packaging metadata standardized: SPDX `license` field replacing the
  deprecated `License ::` classifier, consistent `[project.urls]` keys, and
  populated `keywords`.
- Minimum Python raised to 3.11 (from 3.10, which reaches end of life in
  October 2026).
- Build requirement floor raised to `uv_build>=0.12.0,<0.13.0`.

### Internal

- Ruff configuration adopted the project-family standard (`select = ["ALL"]`
  with a shared ignore list), resolving 29 violations.
- Test directory renamed `test/` to `tests/`.
- CI consolidated into one matrixed `check` job over Python 3.11-3.14 with a
  `version-guard` job; type checking pinned to 3.14.
- Release pipeline replaced: publishing now follows CI success on `main` and
  creates the tag and GitHub release itself, rather than being triggered by a
  manually created release.
- Dependency updates grouped by ecosystem, with a new `pre-commit` ecosystem,
  and minor/patch updates merged automatically.

## [1.0.0] - 2026-03-06

### Added
- `--version` flag on all four CLI commands.
- Accepted input formats and error behavior documented in README.
- `[tool.pytest.ini_options]` in `pyproject.toml` with `--cov-fail-under=100` to enforce 100% coverage in CI.

### Changed
- Improved `--help` text for all commands to document accepted input prefixes (`0b`, `0o`, `0x`, decimal).
- Updated Development Status classifier to `5 - Production/Stable`.
- `Justfile` `setup` recipe updated from `uv pip install -e .[dev]` to `uv sync`.
- CI pytest step simplified — flags now managed via `pyproject.toml`.
- Updated `pre-commit-hooks` from `v4.5.0` to `v6.0.0`.
- Updated `ruff-pre-commit` from `v0.3.4` to `v0.15.5`.

### Removed
- Dead `mirrors-mypy` pre-commit hook (CI uses `ty`).

## [0.2.2] - 2026-03-06

### Changed
- Replaced curl-based uv install in CD workflow with `astral-sh/setup-uv@v6`.

## [0.2.1] - 2026-03-06

### Added
- Tests for invalid input: `ValueError` raised by lib functions, non-zero exit and error message from CLI commands; 100% branch coverage.

### Fixed
- CLI commands now return a clear error message on invalid input instead of crashing (raises `click.BadParameter`).
- Fixed absolute import in `__init__.py` to use a relative import.

### Changed
- Renamed internal CLI functions `bin/oct/dec/hex` to `bin_cmd/oct_cmd/dec_cmd/hex_cmd` to avoid shadowing Python built-ins.
- Pinned `click>=8.0` dependency.
- Enabled ruff `A001` lint rule to catch built-in shadowing.
- Replaced curl-based uv install in CI with the official `astral-sh/setup-uv@v6` action.

### Removed
- Dead `[tool.mypy]` configuration (CI uses `ty`).

## [0.2.0] - 2026-01-13

### Removed
- **Breaking Change**: Removed specific conversion commands:
    - `hextodec`, `hextooct`, `hextobin`
    - `dectohex`, `dectooct`, `dectobin`
    - `octtohex`, `octtodec`, `octtobin`
    - `bintohex`, `bintodec`, `bintooct`

### Added
- **Breaking Change**: Introduced generic conversion commands to replace the removed ones:
    - `bin`: Convert from any base to binary.
    - `oct`: Convert from any base to octal.
    - `dec`: Convert from any base to decimal.
    - `hex`: Convert from any base to hexadecimal.
- Migrated build system to `uv`.

## [0.1.0] - 2026-01-13

### Added
- Initial release of `convbase`.
- Specific command-line utilities for base conversion (e.g., `hextodec`, `bintooct`, etc.).
