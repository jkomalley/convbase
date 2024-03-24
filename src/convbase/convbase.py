from importlib.metadata import version

import click

version_option = click.version_option(
    version(__package__), package_name=__package__, message="%(package)s %(version)s"
)

HEXBASE = 16
DECBASE = 10
OCTBASE = 8
BINBASE = 2


@click.command()
@click.argument("value")
@version_option
def hextodec(value):
    """Convert a hexadecimal value to decimal."""
    try:
        dec_value = int(value, HEXBASE)
    except ValueError:
        click.echo("Error: not hex value")
        exit(1)
    else:
        print(dec_value)


@click.command()
@click.argument("value")
@version_option
def hextooct(value):
    """Convert a hexadecimal value to octal."""
    try:
        dec_value = int(value, HEXBASE)
    except ValueError:
        click.echo("Error: not hex value")
        exit(1)
    else:
        print(oct(dec_value))


@click.command()
@click.argument("value")
@version_option
def hextobin(value):
    """Convert a hexadecimal value to binary."""
    try:
        dec_value = int(value, HEXBASE)
    except ValueError:
        click.echo("Error: not hex value")
        exit(1)
    else:
        print(bin(dec_value))


@click.command()
@click.argument("value")
@version_option
def dectohex(value):
    """Convert a decimal value to hexadecimal."""
    try:
        dec_value = int(value, DECBASE)
    except ValueError:
        click.echo("Error: not decimal value")
        exit(1)
    else:
        print(hex(dec_value))


@click.command()
@click.argument("value")
@version_option
def dectooct(value):
    """Convert a decimal value to octal."""
    try:
        dec_value = int(value, DECBASE)
    except ValueError:
        click.echo("Error: not decimal value")
        exit(1)
    else:
        print(oct(dec_value))


@click.command()
@click.argument("value")
@version_option
def dectobin(value):
    """Convert a decimal value to binary."""
    try:
        dec_value = int(value, DECBASE)
    except ValueError:
        click.echo("Error: not decimal value")
        exit(1)
    else:
        print(bin(dec_value))


@click.command()
@click.argument("value")
@version_option
def octtohex(value):
    """Convert an octal value to hexadecimal."""
    try:
        dec_value = int(value, OCTBASE)
    except ValueError:
        click.echo("Error: not octal value")
        exit(1)
    else:
        print(hex(dec_value))


@click.command()
@click.argument("value")
@version_option
def octtodec(value):
    """Convert an octal value to decimal."""
    try:
        dec_value = int(value, OCTBASE)
    except ValueError:
        click.echo("Error: not octal value")
        exit(1)
    else:
        print(dec_value)


@click.command()
@click.argument("value")
@version_option
def octtobin(value):
    """Convert an octal value to binary."""
    try:
        dec_value = int(value, OCTBASE)
    except ValueError:
        click.echo("Error: not octal value")
        exit(1)
    else:
        print(bin(dec_value))


@click.command()
@click.argument("value")
@version_option
def bintohex(value):
    """Convert a binary value to hexadecimal."""
    try:
        dec_value = int(value, BINBASE)
    except ValueError:
        click.echo("Error: not binary value")
        exit(1)
    else:
        print(hex(dec_value))


@click.command()
@click.argument("value")
@version_option
def bintodec(value):
    """Convert a binnary value to decimal."""
    try:
        dec_value = int(value, BINBASE)
    except ValueError:
        click.echo("Error: not binary value")
        exit(1)
    else:
        print(dec_value)


@click.command()
@click.argument("value")
@version_option
def bintooct(value):
    """Convert a binary value to octal."""
    try:
        dec_value = int(value, BINBASE)
    except ValueError:
        click.echo("Error: not binary value")
        exit(1)
    else:
        print(oct(dec_value))
