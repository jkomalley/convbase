def to_binary(value: str) -> str:
    return bin(int(value, 0))


def to_octal(value: str) -> str:
    return oct(int(value, 0))


def to_decimal(value: str) -> str:
    return str(int(value, 0))


def to_hexadecimal(value: str) -> str:
    return hex(int(value, 0))
