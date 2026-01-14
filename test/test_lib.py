import pytest
from convbase import lib


@pytest.mark.parametrize(
    "value, expected",
    [("10", "0b1010"), ("0b1010", "0b1010"), ("0o12", "0b1010"), ("0xA", "0b1010")],
)
def test_to_binary(value, expected):
    assert lib.to_binary(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [("10", "0o12"), ("0b1010", "0o12"), ("0o12", "0o12"), ("0xA", "0o12")],
)
def test_to_octal(value, expected):
    assert lib.to_octal(value) == expected


@pytest.mark.parametrize(
    "value, expected", [("10", "10"), ("0b1010", "10"), ("0o12", "10"), ("0xA", "10")]
)
def test_to_decimal(value, expected):
    assert lib.to_decimal(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [("10", "0xa"), ("0b1010", "0xa"), ("0o12", "0xa"), ("0xA", "0xa")],
)
def test_to_hexadecimal(value, expected):
    assert lib.to_hexadecimal(value) == expected.lower()
