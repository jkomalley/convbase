def to_binary(value: str) -> str:
    """Convert a numeric string to its binary representation.

    Args:
        value: A decimal integer, or one prefixed with 0b, 0o, or 0x.

    Returns:
        The value as a 0b-prefixed binary string.

    Raises:
        ValueError: If value is not a valid integer literal.
    """
    return bin(int(value, 0))


def to_octal(value: str) -> str:
    """Convert a numeric string to its octal representation.

    Args:
        value: A decimal integer, or one prefixed with 0b, 0o, or 0x.

    Returns:
        The value as a 0o-prefixed octal string.

    Raises:
        ValueError: If value is not a valid integer literal.
    """
    return oct(int(value, 0))


def to_decimal(value: str) -> str:
    """Convert a numeric string to its decimal representation.

    Args:
        value: A decimal integer, or one prefixed with 0b, 0o, or 0x.

    Returns:
        The value as an unprefixed decimal string.

    Raises:
        ValueError: If value is not a valid integer literal.
    """
    return str(int(value, 0))


def to_hexadecimal(value: str) -> str:
    """Convert a numeric string to its hexadecimal representation.

    Args:
        value: A decimal integer, or one prefixed with 0b, 0o, or 0x.

    Returns:
        The value as a 0x-prefixed lowercase hexadecimal string.

    Raises:
        ValueError: If value is not a valid integer literal.
    """
    return hex(int(value, 0))
