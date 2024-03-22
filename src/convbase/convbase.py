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
def dectohex():
    pass

@click.command()
@click.argument("value")
@version_option
def dectooct():
    pass

@click.command()
@click.argument("value")
@version_option
def dectobin():
    pass

@click.command()
@click.argument("value")
@version_option
def octtohex():
    pass

@click.command()
@click.argument("value")
@version_option
def octtodec():
    pass

@click.command()
@click.argument("value")
@version_option
def octtobin():
    pass

@click.command()
@click.argument("value")
@version_option
def bintohex():
    pass

@click.command()
@click.argument("value")
@version_option
def bintodec():
    pass

@click.command()
@click.argument("value")
@version_option
def bintooct():
    pass
