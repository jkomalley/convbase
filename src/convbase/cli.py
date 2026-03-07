import click

from . import lib


@click.command()
@click.argument("value")
def bin_cmd(value):
    """Converts a value to binary."""
    try:
        click.echo(lib.to_binary(value))
    except ValueError:
        raise click.BadParameter(f"invalid integer: {value!r}", param_hint="VALUE")


@click.command()
@click.argument("value")
def oct_cmd(value):
    """Converts a value to octal."""
    try:
        click.echo(lib.to_octal(value))
    except ValueError:
        raise click.BadParameter(f"invalid integer: {value!r}", param_hint="VALUE")


@click.command()
@click.argument("value")
def dec_cmd(value):
    """Converts a value to decimal."""
    try:
        click.echo(lib.to_decimal(value))
    except ValueError:
        raise click.BadParameter(f"invalid integer: {value!r}", param_hint="VALUE")


@click.command()
@click.argument("value")
def hex_cmd(value):
    """Converts a value to hexadecimal."""
    try:
        click.echo(lib.to_hexadecimal(value))
    except ValueError:
        raise click.BadParameter(f"invalid integer: {value!r}", param_hint="VALUE")
