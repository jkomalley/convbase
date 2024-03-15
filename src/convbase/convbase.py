from importlib.metadata import version

import click

__version__ = version(__package__)

PREFIXES = ["0x", "0d", "0o", "0b"]
BASESTRS = ["HEX", "DEC", "OCT", "BIN"]
BASES = [16, 10, 8, 2]
PREFIX_TO_BASE = {p: b for p, b in zip(PREFIXES, BASES)}
BASESTR_TO_BASE = {b: bn for b, bn in zip(BASESTRS, BASES)}

HEX = "0123456789abcdef"
DEC = "0123456789"
OCT = "01234567"
BIN = "01"


def _containsOnly(e: str, s: str):
    """returns true if all chars in e are in s, false otherwise."""
    return set(e) <= set(s)


def _validate_number(ctx, param, value):
    value = value.lower()

    match value[:2]:
        case "0x":
            # number can be a hex prefixed with 0x or 0X (normalize to the latter)
            if not _containsOnly(value[2:], HEX):
                raise click.BadParameter(
                    f"hex (0x) values can only contain digits {HEX}"
                )
        case "0o":
            # number can be an oct prefixed with 0o or 0O (normalize to the latter)
            if not _containsOnly(value[2:], OCT):
                raise click.BadParameter(
                    f"oct (0o) values can only contain digits {OCT}"
                )
        case "0b":
            # number can be a bin prefixed with 0b or 0B (normalize to the latter)
            if not _containsOnly(value[2:], BIN):
                raise click.BadParameter(
                    f"bin (0b) values can only contain digits {BIN}"
                )
        case "0d":
            # number can be a bin prefixed with 0b or 0B (normalize to the latter)
            if not _containsOnly(value[2:], DEC):
                raise click.BadParameter(
                    f"dec (0d) values can only contain digits {DEC}"
                )
        case _:
            # number can be a dec with no prefix
            if not _containsOnly(value, DEC):
                raise click.BadParameter(f"dec values can only contain digits {DEC}")
            else:
                value = "0d" + value
        
    if len(value) <= 2:
        raise click.BadParameter(f"'{value}'")
    
    return value


def getBaseFromNumber(number: str) -> int:
    try:
        prefix = number[:2]
        base = PREFIX_TO_BASE[prefix]
    except KeyError:
        raise ValueError("arg number has invalid prefix")
    
    return base


def getBaseFromBaseStr(baseStr: str) -> int:
    try:
        basenum = BASESTR_TO_BASE[baseStr]
    except KeyError:
        raise ValueError(f"invalid arg baseStr '{baseStr}'")
    
    return basenum


def convertBase(inBase: int, numStr: str, outBase: int) -> str:
    num = int(numStr, inBase)

    match outBase:
        case 16:
            return hex(num)
        case 10:
            return str(num)
        case 8:
            return oct(num)
        case 2:
            return bin(num)
        case _:
            raise ValueError(f"outBase {outBase} not in {BASES}")


@click.command()
@click.version_option(
    __version__, package_name=__package__, message="%(package)s %(version)s"
)
@click.argument("number", callback=_validate_number)
@click.option(
    "-o",
    "--output",
    "outBaseStr",
    type=click.Choice(BASES, case_sensitive=False),
    required=True,
    help="The base to convert NUMBER to.",
)
def run(number, outBaseStr):
    """Convert NUMBER to the given output base.

    NUMBER: value to convert (prefixed with 0x, 0o, 0b or none for decimal).
    """
    inBase = getBaseFromNumber(number)
    outBase = getBaseFromBaseStr(outBaseStr)
    convertedNumber = convertBase(inBase, number, outBase)
    print(f"{convertedNumber}")

