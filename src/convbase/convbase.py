from importlib.metadata import version

import click

__version__ = version(__package__)


@click.command()
@click.version_option(
    __version__, package_name=__package__, message="%(package)s %(version)s"
)
def run():
    pass
