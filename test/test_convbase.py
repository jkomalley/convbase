from click.testing import CliRunner
from convbase import convbase, __version__


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(convbase.run, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"{convbase.__package__} {__version__}\n"
