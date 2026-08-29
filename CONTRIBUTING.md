# Contributing to convbase

Thanks for your interest in improving `convbase`. This guide covers everything
you need to get set up and land a change. For *usage*, see the
[README](README.md).

## Ways to contribute

- **Report a bug** or **request a feature** by [opening an issue](https://github.com/jkomalley/convbase/issues).
- **Submit a pull request** for a fix or improvement.

For anything large or behavior-changing, please open an issue to discuss the
approach before investing time in a PR.

## Development setup

**Prerequisites:** Python 3.11+ and [`uv`](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/jkomalley/convbase.git
cd convbase
just install               # uv sync + pre-commit install
```

Or without `just`:

```bash
uv sync                    # create the venv and install all dependencies
uv run pre-commit install  # enable the git hooks
```

## Project layout

The package uses a `src/` layout:

| Module | Responsibility |
| --- | --- |
| `lib.py` | Pure conversion functions (`to_binary`, `to_octal`, `to_decimal`, `to_hexadecimal`). No click, no I/O. |
| `cli.py` | The four click entry points — one console script per output base. Translates `ValueError` into `click.BadParameter`. |
| `__init__.py` | The public API surface (re-exports the four `to_*` functions). |

Every command parses its input with `int(value, 0)`, which is why all four accept
the same formats: bare decimal, or `0b` / `0o` / `0x` prefixed. Keep conversion
logic in `lib.py` — `cli.py` should stay a thin wrapper.

## Running checks

The repo uses [`just`](https://github.com/casey/just) as a task runner. Run
everything before pushing:

```bash
just check      # format-check + lint-check + typecheck + tests
```

Or run individual tasks:

```bash
just format     # ruff format src/ tests/
just lint       # ruff check --fix src/ tests/
just typecheck  # ty check src/
just test       # pytest
```

Each task maps to a plain `uv run …` command, so you can run them directly if
you'd rather not install `just`.

## Coding standards

- **Style & linting:** [`ruff`](https://docs.astral.sh/ruff/) with all rules
  enabled (see `pyproject.toml` for the pragmatic exceptions). Run `just format`
  and `just lint` before committing.
- **Type checking:** the codebase is fully typed; `just typecheck` must pass.
- **Docstrings:** Google-style, on every public function.
- **Comments:** explain *why*, not *what*.
- **Line length:** 88 characters.
- **Commits:** Conventional Commits (`feat`, `fix`, `docs`, `chore`, `refactor`,
  `test`, `ci`, `deps`, `style`), one logical change each.

### Testing

- **100% coverage is required.** The gate lives in `[tool.pytest.ini_options]`
  `addopts`, so a plain `uv run pytest` enforces it — locally and in CI.
- Conversion behavior is tested directly against `lib`; CLI behavior is tested
  through click's `CliRunner`.
- Ruff enforces `PT006`, so `pytest.mark.parametrize` takes a **tuple** of
  names: `("value", "expected")`.

## Pull requests

- Branch off `main`; one logical change per PR.
- Include tests for any new or changed behavior.
- Make sure `just check` passes cleanly before you open the PR.
- PRs are **rebase-merged**; squash and merge commits are disabled.

CI runs the full check suite against Python 3.11–3.14 on every pull request.

## Releasing

Releases are published to PyPI automatically: the CD workflow fires when CI
passes on `main` and publishes whenever `pyproject.toml`'s version isn't already
on PyPI. So a release is just a version bump merged to `main`.

Choose the bump from the changes since the **last release tag**, not just your
latest work:

```bash
git log "$(git describe --tags --abbrev=0)"..HEAD --oneline
```

Map the conventional-commit types in that range to a [semver](https://semver.org/)
bump and apply it:

| Changes since last release | Bump | Command |
| --- | --- | --- |
| Any `feat:` | minor | `just bump-version minor` |
| Only `fix:` / `docs:` / `chore:` | patch | `just bump-version patch` |
| A breaking change (`feat!:`, `BREAKING CHANGE`) | major | `just bump-version major` |

Open the bump as its own PR. The `version-guard` CI job enforces this: it fails
any release PR whose bump is too small for the commits since the last release
(for example, shipping a `feat:` in a patch). Features merged to `main` without
a release accumulate, so the bump must account for all of them — not just the
most recent change.

Release notes are taken from the matching `## [x.y.z]` section of
`CHANGELOG.md`. **A missing section aborts the release before publishing**, so
rename `## [Unreleased]` to `## [X.Y.Z] - <date>` in the same PR as the bump.

## License

By contributing, you agree that your contributions are licensed under the
project's [MIT License](LICENSE).
