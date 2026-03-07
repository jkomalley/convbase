from click.testing import CliRunner
import pytest
from convbase.cli import bin_cmd, oct_cmd, dec_cmd, hex_cmd


@pytest.fixture
def runner():
    return CliRunner()


@pytest.mark.parametrize(
    "value, expected",
    [("10", "0b1010"), ("0b1010", "0b1010"), ("0o12", "0b1010"), ("0xA", "0b1010")],
)
def test_bin_command(runner, value, expected):
    result = runner.invoke(bin_cmd, [value])
    assert result.exit_code == 0
    assert result.output.strip() == expected


@pytest.mark.parametrize(
    "value, expected",
    [("10", "0o12"), ("0b1010", "0o12"), ("0o12", "0o12"), ("0xA", "0o12")],
)
def test_oct_command(runner, value, expected):
    result = runner.invoke(oct_cmd, [value])
    assert result.exit_code == 0
    assert result.output.strip() == expected


@pytest.mark.parametrize(
    "value, expected", [("10", "10"), ("0b1010", "10"), ("0o12", "10"), ("0xA", "10")]
)
def test_dec_command(runner, value, expected):
    result = runner.invoke(dec_cmd, [value])
    assert result.exit_code == 0
    assert result.output.strip() == expected


@pytest.mark.parametrize(
    "value, expected",
    [("10", "0xa"), ("0b1010", "0xa"), ("0o12", "0xa"), ("0xA", "0xa")],
)
def test_hex_command(runner, value, expected):
    result = runner.invoke(hex_cmd, [value])
    assert result.exit_code == 0
    assert result.output.strip() == expected.lower()


@pytest.mark.parametrize("cmd", [bin_cmd, oct_cmd, dec_cmd, hex_cmd])
def test_invalid_input_exits_nonzero(runner, cmd):
    result = runner.invoke(cmd, ["hello"])
    assert result.exit_code != 0
    assert "Invalid value" in result.output
