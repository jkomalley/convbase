import nox


@nox.session(python="3.10", venv_backend="uv")
def lint(session):
    session.install("ruff")
    session.run("ruff", "check", "--fix")
    session.run("ruff", "format")


@nox.session(python=["3.10", "3.11", "3.12"], venv_backend="uv")
def test(session):
    session.install("pytest")
    session.install(".")
    session.run("pytest", "-q")
