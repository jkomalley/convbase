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


@pytest.mark.parametrize(
    "input, expected",
    [
        ("0", "0x0"),
        ("1", "0x1"),
        ("2", "0x2"),
        ("3", "0x3"),
        ("4", "0x4"),
        ("5", "0x5"),
        ("6", "0x6"),
        ("7", "0x7"),
        ("8", "0x8"),
        ("9", "0x9"),
        ("10", "0xa"),
        ("11", "0xb"),
        ("12", "0xc"),
        ("13", "0xd"),
        ("14", "0xe"),
        ("15", "0xf"),
    ],
)
def test_command_dectohex_valid(runner, input, expected):
    res = runner.invoke(convbase.dectohex, input)
    assert res.exit_code == 0
    assert res.output == f"{expected}\n"


@pytest.mark.parametrize("input", ["one", "4f", "4O", "W0W"])
def test_command_dectohex_invalid(runner, input):
    res = runner.invoke(convbase.dectohex, input)
    assert res.exit_code == 1
    assert res.output == "Error: not decimal value\n"


@pytest.mark.parametrize(
    "input, expected",
    [
        ("0", "0o0"),
        ("1", "0o1"),
        ("2", "0o2"),
        ("3", "0o3"),
        ("4", "0o4"),
        ("5", "0o5"),
        ("6", "0o6"),
        ("7", "0o7"),
        ("8", "0o10"),
        ("9", "0o11"),
        ("10", "0o12"),
    ],
)
def test_command_dectooct_valid(runner, input, expected):
    res = runner.invoke(convbase.dectooct, input)
    assert res.exit_code == 0
    assert res.output == f"{expected}\n"


@pytest.mark.parametrize("input", ["one", "4f", "4O", "W0W"])
def test_command_dectooct_invalid(runner, input):
    res = runner.invoke(convbase.dectooct, input)
    assert res.exit_code == 1
    assert res.output == "Error: not decimal value\n"


@pytest.mark.parametrize(
    "input, expected",
    [
        ("0", "0b0"),
        ("1", "0b1"),
        ("2", "0b10"),
        ("3", "0b11"),
        ("4", "0b100"),
        ("5", "0b101"),
        ("6", "0b110"),
        ("7", "0b111"),
        ("8", "0b1000"),
        ("9", "0b1001"),
        ("10", "0b1010"),
    ],
)
def test_command_dectobin_valid(runner, input, expected):
    res = runner.invoke(convbase.dectobin, input)
    assert res.exit_code == 0
    assert res.output == f"{expected}\n"


@pytest.mark.parametrize("input", ["one", "4f", "4O", "W0W"])
def test_command_dectobin_invalid(runner, input):
    res = runner.invoke(convbase.dectobin, input)
    assert res.exit_code == 1
    assert res.output == "Error: not decimal value\n"


@pytest.mark.parametrize(
    "input, expected",
    [
        ("0o0", "0x0"),
        ("0o1", "0x1"),
        ("0o2", "0x2"),
        ("0o3", "0x3"),
        ("0o4", "0x4"),
        ("0o5", "0x5"),
        ("0o6", "0x6"),
        ("0o7", "0x7"),
    ],
)
def test_command_octtohex_valid(runner, input, expected):
    res = runner.invoke(convbase.octtohex, input)
    assert res.exit_code == 0
    assert res.output == f"{expected}\n"


@pytest.mark.parametrize("input", ["one", "4f", "4O", "0OF"])
def test_command_octtohex_invalid(runner, input):
    res = runner.invoke(convbase.octtohex, input)
    assert res.exit_code == 1
    assert res.output == "Error: not octal value\n"


@pytest.mark.parametrize(
    "input, expected",
    [
        ("0o0", "0"),
        ("0o1", "1"),
        ("0o2", "2"),
        ("0o3", "3"),
        ("0o4", "4"),
        ("0o5", "5"),
        ("0o6", "6"),
        ("0o7", "7"),
        ("0o10", "8"),
        ("0o11", "9"),
        ("0o12", "10"),
    ],
)
def test_command_octtodec_valid(runner, input, expected):
    res = runner.invoke(convbase.octtodec, input)
    assert res.exit_code == 0
    assert res.output == f"{expected}\n"


@pytest.mark.parametrize("input", ["one", "4f", "4O", "0OF"])
def test_command_octtodec_invalid(runner, input):
    res = runner.invoke(convbase.octtodec, input)
    assert res.exit_code == 1
    assert res.output == "Error: not octal value\n"


@pytest.mark.parametrize(
    "input, expected",
    [
        ("0o0", "0b0"),
        ("0o1", "0b1"),
        ("0o2", "0b10"),
        ("0o3", "0b11"),
        ("0o4", "0b100"),
        ("0o5", "0b101"),
        ("0o6", "0b110"),
        ("0o7", "0b111"),
        ("0o10", "0b1000"),
        ("0o11", "0b1001"),
        ("0o12", "0b1010"),
    ],
)
def test_command_octtobin_valid(runner, input, expected):
    res = runner.invoke(convbase.octtobin, input)
    assert res.exit_code == 0
    assert res.output == f"{expected}\n"


@pytest.mark.parametrize("input", ["one", "4f", "4O", "0OF"])
def test_command_octtobin_invalid(runner, input):
    res = runner.invoke(convbase.octtobin, input)
    assert res.exit_code == 1
    assert res.output == "Error: not octal value\n"


@pytest.mark.parametrize(
    "input, expected",
    [
        ("0b0", "0x0"),
        ("0b1", "0x1"),
        ("0b10", "0x2"),
        ("0b11", "0x3"),
        ("0b100", "0x4"),
        ("0b101", "0x5"),
        ("0b110", "0x6"),
        ("0b111", "0x7"),
        ("0b1000", "0x8"),
        ("0b1001", "0x9"),
        ("0b1010", "0xa"),
        ("0b1011", "0xb"),
        ("0b1100", "0xc"),
        ("0b1101", "0xd"),
        ("0b1110", "0xe"),
        ("0b1111", "0xf"),
    ],
)
def test_command_bintohex_valid(runner, input, expected):
    res = runner.invoke(convbase.bintohex, input)
    assert res.exit_code == 0
    assert res.output == f"{expected}\n"


@pytest.mark.parametrize("input", ["B00", "00b1", "1O1O", "2"])
def test_command_bintohex_invalid(runner, input):
    res = runner.invoke(convbase.bintohex, input)
    assert res.exit_code == 1
    assert res.output == "Error: not binary value\n"


# TODO: test bintodec
@pytest.mark.parametrize(
    "input, expected",
    [
        ("0b0", "0"),
        ("0b1", "1"),
        ("0b10", "2"),
        ("0b11", "3"),
        ("0b100", "4"),
        ("0b101", "5"),
        ("0b110", "6"),
        ("0b111", "7"),
        ("0b1000", "8"),
        ("0b1001", "9"),
        ("0b1010", "10"),
        ("0b1011", "11"),
        ("0b1100", "12"),
        ("0b1101", "13"),
        ("0b1110", "14"),
        ("0b1111", "15"),
    ],
)
def test_command_bintodec_valid(runner, input, expected):
    res = runner.invoke(convbase.bintodec, input)
    assert res.exit_code == 0
    assert res.output == f"{expected}\n"


@pytest.mark.parametrize("input", ["B00", "00b1", "1O1O", "2"])
def test_command_bintodec_invalid(runner, input):
    res = runner.invoke(convbase.bintodec, input)
    assert res.exit_code == 1
    assert res.output == "Error: not binary value\n"


# TODO: test bintooct
@pytest.mark.parametrize(
    "input, expected",
    [
        ("0b0", "0o0"),
        ("0b1", "0o1"),
        ("0b10", "0o2"),
        ("0b11", "0o3"),
        ("0b100", "0o4"),
        ("0b101", "0o5"),
        ("0b110", "0o6"),
        ("0b111", "0o7"),
        ("0b1000", "0o10"),
        ("0b1001", "0o11"),
        ("0b1010", "0o12"),
        ("0b1011", "0o13"),
        ("0b1100", "0o14"),
        ("0b1101", "0o15"),
        ("0b1110", "0o16"),
        ("0b1111", "0o17"),
    ],
)
def test_command_bintooct_valid(runner, input, expected):
    res = runner.invoke(convbase.bintooct, input)
    assert res.exit_code == 0
    assert res.output == f"{expected}\n"


@pytest.mark.parametrize("input", ["B00", "00b1", "1O1O", "2"])
def test_command_bintooct_invalid(runner, input):
    res = runner.invoke(convbase.bintooct, input)
    assert res.exit_code == 1
    assert res.output == "Error: not binary value\n"


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
