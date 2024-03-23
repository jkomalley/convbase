from click.testing import CliRunner
import pytest
from convbase import convbase, __version__


@pytest.fixture
def runner():
    return CliRunner()


@pytest.mark.parametrize(
    "input, expected",
    [
        ("0x0", "0"),
        ("0x1", "1"),
        ("0x2", "2"),
        ("0x3", "3"),
        ("0x4", "4"),
        ("0x5", "5"),
        ("0x6", "6"),
        ("0x7", "7"),
        ("0x8", "8"),
        ("0x9", "9"),
        ("0xA", "10"),
        ("0xB", "11"),
        ("0xC", "12"),
        ("0xD", "13"),
        ("0xE", "14"),
        ("0xF", "15"),
        ("0X64", "100"),
        ("0xff", "255"),
        ("0Xff", "255"),
        ("FF", "255"),
    ],
)
def test_command_hextodec_valid(runner, input, expected):
    res = runner.invoke(convbase.hextodec, input)
    assert res.exit_code == 0
    assert res.output == f"{expected}\n"


@pytest.mark.parametrize("input", ["00x0", "Ox1", "0xX", "0xdeadbeer"])
def test_command_hextodec_invalid(runner, input):
    res = runner.invoke(convbase.hextodec, input)
    print(res.output)
    assert res.exit_code == 1
    assert res.output == "Error: not hex value\n"


@pytest.mark.parametrize(
    "input, expected",
    [
        ("0x0", "0o0"),
        ("0x1", "0o1"),
        ("0x2", "0o2"),
        ("0x3", "0o3"),
        ("0x4", "0o4"),
        ("0x5", "0o5"),
        ("0x6", "0o6"),
        ("0x7", "0o7"),
        ("0x8", "0o10"),
        ("0x9", "0o11"),
        ("0xA", "0o12"),
        ("0xB", "0o13"),
        ("0xC", "0o14"),
        ("0xD", "0o15"),
        ("0xE", "0o16"),
        ("0xF", "0o17"),
        ("0X64", "0o144"),
        ("0xff", "0o377"),
        ("0Xff", "0o377"),
        ("FF", "0o377"),
    ],
)
def test_command_hextooct_valid(runner, input, expected):
    res = runner.invoke(convbase.hextooct, input)
    assert res.exit_code == 0
    assert res.output == f"{expected}\n"


@pytest.mark.parametrize("input", ["00x0", "Ox1", "0xX", "0xdeadbeer"])
def test_command_hextooct_invalid(runner, input):
    res = runner.invoke(convbase.hextooct, input)
    assert res.exit_code == 1
    assert res.output == "Error: not hex value\n"


@pytest.mark.parametrize(
    "input, expected",
    [
        ("0x0", "0b0"),
        ("0x1", "0b1"),
        ("0x2", "0b10"),
        ("0x3", "0b11"),
        ("0x4", "0b100"),
        ("0x5", "0b101"),
        ("0x6", "0b110"),
        ("0x7", "0b111"),
        ("0x8", "0b1000"),
        ("0x9", "0b1001"),
        ("0xA", "0b1010"),
        ("0xB", "0b1011"),
        ("0xC", "0b1100"),
        ("0xD", "0b1101"),
        ("0xE", "0b1110"),
        ("0xF", "0b1111"),
        ("0X64", "0b1100100"),
        ("0xff", "0b11111111"),
        ("0Xff", "0b11111111"),
        ("FF", "0b11111111"),
    ],
)
def test_command_hextobin_valid(runner, input, expected):
    res = runner.invoke(convbase.hextobin, input)
    assert res.exit_code == 0
    assert res.output == f"{expected}\n"


@pytest.mark.parametrize("input", ["00x0", "Ox1", "0xX", "0xdeadbeer"])
def test_command_hextobin_invalid(runner, input):
    res = runner.invoke(convbase.hextobin, input)
    assert res.exit_code == 1
    assert res.output == "Error: not hex value\n"


def test_test_version(runner):
    result = runner.invoke(convbase.hextodec, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"{convbase.__package__} {__version__}\n"

    result = runner.invoke(convbase.hextooct, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"{convbase.__package__} {__version__}\n"

    result = runner.invoke(convbase.hextobin, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"{convbase.__package__} {__version__}\n"

    result = runner.invoke(convbase.dectohex, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"{convbase.__package__} {__version__}\n"

    result = runner.invoke(convbase.dectooct, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"{convbase.__package__} {__version__}\n"

    result = runner.invoke(convbase.dectobin, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"{convbase.__package__} {__version__}\n"

    result = runner.invoke(convbase.octtohex, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"{convbase.__package__} {__version__}\n"

    result = runner.invoke(convbase.octtodec, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"{convbase.__package__} {__version__}\n"

    result = runner.invoke(convbase.octtobin, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"{convbase.__package__} {__version__}\n"

    result = runner.invoke(convbase.hextodec, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"{convbase.__package__} {__version__}\n"

    result = runner.invoke(convbase.hextodec, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"{convbase.__package__} {__version__}\n"

    result = runner.invoke(convbase.hextodec, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"{convbase.__package__} {__version__}\n"
