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
    try:
        dec_value = int(value, BINBASE)
    except ValueError:
        click.echo("Error: not binary value")
        exit(1)
    else:
        print(oct(dec_value))
