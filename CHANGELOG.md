# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
