from importlib.metadata import version

import click

__version__ = version(__package__)

PREFIXES = ["0x", "0d", "0o", "0b"]
BASES = ["HEX", "DEC", "OCT", "BIN"]
BASENUMS = [16, 10, 8, 2]
PREFIX_TO_BASE = {p: b for p, b in zip(PREFIXES, BASES)}
BASE_TO_BASENUM = {b: bn for b, bn in zip(BASES, BASENUMS)}

HEX = "0123456789abcdef"
DEC = "0123456789"
OCT = "01234567"
BIN = "01"


def _containsOnly(e: str, s: str):
    """returns true if all chars in e are in s, false otherwise."""
    return set(e) <= set(s)


def _validate_number(ctx, param, value: str):
    value = value.lower()

    match value[:2]:
        case "0x":
            # number can be a hex prefixed with 0x or 0X (normalize to the latter)
            if _containsOnly(value[2:], HEX):
                return value
            else:
                raise click.BadParameter(
                    f"hex (0x) values can only contain digits {HEX}"
                )
        case "0o":
            # number can be an oct prefixed with 0o or 0O (normalize to the latter)
            if _containsOnly(value[2:], OCT):
                return value
            else:
                raise click.BadParameter(
                    f"oct (0o) values can only contain digits {OCT}"
                )
        case "0b":
            # number can be a bin prefixed with 0b or 0B (normalize to the latter)
            if _containsOnly(value[2:], BIN):
                return value
            else:
                raise click.BadParameter(
                    f"bin (0b) values can only contain digits {BIN}"
                )
        case _:
            # number can be a dec with no prefix
            if _containsOnly(value, DEC):
                return "0d" + value
            else:
                raise click.BadParameter(f"dec values can only contain digits {DEC}")


def getBaseFromPrefix(number: str) -> str | None:
    try:
        prefix = number[:2]
        return PREFIX_TO_BASE[prefix]
    except KeyError:
        return None


def convertBase(inBase: str, inNumber: str, outBase: str):
    inBaseNum = BASE_TO_BASENUM[inBase]

    inNumInt = int(inNumber, inBaseNum)

    match outBase:
        case "HEX":
            return hex(inNumInt)
        case "DEC":
            return str(inNumInt)
        case "OCT":
            return oct(inNumInt)
        case "BIN":
            return bin(inNumInt)
        case _:
            raise ValueError(f"outBase must be one of {BASES}")


@click.command()
@click.version_option(
    __version__, package_name=__package__, message="%(package)s %(version)s"
)
@click.argument("number", callback=_validate_number)
@click.option(
    "-o",
    "--output-base",
    "outBase",
    type=click.Choice(BASES, case_sensitive=False),
    required=True,
    help="The base to convert NUMBER to.",
)
def run(number, outBase):
    """Convert NUMBER to the given output base.

    NUMBER: value to convert (prefixed with 0x, 0o, 0b or none for decimal).
    """
    inBase = getBaseFromPrefix(number)
    convertedNumber = convertBase(inBase, number, outBase)
    print(f"{convertedNumber}")

