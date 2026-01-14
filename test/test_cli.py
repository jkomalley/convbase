from click.testing import CliRunner
import pytest
from convbase import cli


@pytest.fixture
def runner():
    return CliRunner()


@pytest.mark.parametrize(
    "value, expected",
    [("10", "0b1010"), ("0b1010", "0b1010"), ("0o12", "0b1010"), ("0xA", "0b1010")],
)
def test_bin_command(runner, value, expected):
    result = runner.invoke(cli.bin, [value])
    assert result.exit_code == 0
    assert result.output.strip() == expected


@pytest.mark.parametrize(
    "value, expected",
    [("10", "0o12"), ("0b1010", "0o12"), ("0o12", "0o12"), ("0xA", "0o12")],
)
def test_oct_command(runner, value, expected):
    result = runner.invoke(cli.oct, [value])
    assert result.exit_code == 0
    assert result.output.strip() == expected


@pytest.mark.parametrize(
    "value, expected", [("10", "10"), ("0b1010", "10"), ("0o12", "10"), ("0xA", "10")]
)
def test_dec_command(runner, value, expected):
    result = runner.invoke(cli.dec, [value])
    assert result.exit_code == 0
    assert result.output.strip() == expected


@pytest.mark.parametrize(
    "value, expected",
    [("10", "0xa"), ("0b1010", "0xa"), ("0o12", "0xa"), ("0xA", "0xa")],
)
def test_hex_command(runner, value, expected):
    result = runner.invoke(cli.hex, [value])
    assert result.exit_code == 0
    assert result.output.strip() == expected.lower()
