import click

from . import lib


@click.command()
@click.argument("value")
def bin(value):
    """Converts a value to binary."""
    click.echo(lib.to_binary(value))


@click.command()
@click.argument("value")
def oct(value):
    """Converts a value to octal."""
    click.echo(lib.to_octal(value))


@click.command()
@click.argument("value")
def dec(value):
    """Converts a value to decimal."""
    click.echo(lib.to_decimal(value))


@click.command()
@click.argument("value")
def hex(value):
    """Converts a value to hexadecimal."""
    click.echo(lib.to_hexadecimal(value))
