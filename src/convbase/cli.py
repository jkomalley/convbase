import click

from . import lib


@click.command()
@click.version_option(package_name="convbase")
@click.argument("value")
def bin_cmd(value: str) -> None:
    """Convert VALUE to binary.

    VALUE may be a decimal integer or prefixed: 0b (binary), 0o (octal),
    0x (hexadecimal).
    """
    try:
        click.echo(lib.to_binary(value))
    except ValueError as err:
        raise click.BadParameter(
            f"invalid integer: {value!r}", param_hint="VALUE"
        ) from err


@click.command()
@click.version_option(package_name="convbase")
@click.argument("value")
def oct_cmd(value: str) -> None:
    """Convert VALUE to octal.

    VALUE may be a decimal integer or prefixed: 0b (binary), 0o (octal),
    0x (hexadecimal).
    """
    try:
        click.echo(lib.to_octal(value))
    except ValueError as err:
        raise click.BadParameter(
            f"invalid integer: {value!r}", param_hint="VALUE"
        ) from err


@click.command()
@click.version_option(package_name="convbase")
@click.argument("value")
def dec_cmd(value: str) -> None:
    """Convert VALUE to decimal.

    VALUE may be a decimal integer or prefixed: 0b (binary), 0o (octal),
    0x (hexadecimal).
    """
    try:
        click.echo(lib.to_decimal(value))
    except ValueError as err:
        raise click.BadParameter(
            f"invalid integer: {value!r}", param_hint="VALUE"
        ) from err


@click.command()
@click.version_option(package_name="convbase")
@click.argument("value")
def hex_cmd(value: str) -> None:
    """Convert VALUE to hexadecimal.

    VALUE may be a decimal integer or prefixed: 0b (binary), 0o (octal),
    0x (hexadecimal).
    """
    try:
        click.echo(lib.to_hexadecimal(value))
    except ValueError as err:
        raise click.BadParameter(
            f"invalid integer: {value!r}", param_hint="VALUE"
        ) from err
