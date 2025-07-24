"""Main CLI entry point for TypeID CLI."""

import click

from .commands import TypeIDCommands


@click.group()
@click.version_option()
def cli() -> None:
    """CLI tool for TypeID and UUID conversions."""
    pass


@cli.command("typeid-to-uuid")
@click.argument("typeid")
def typeid_to_uuid(typeid: str) -> None:
    """Convert TypeID to UUID7 format."""
    TypeIDCommands.convert_typeid_to_uuid(typeid)


@cli.command("uuid-to-typeid")
@click.argument("uuid")
@click.argument("prefix")
def uuid_to_typeid(uuid: str, prefix: str) -> None:
    """Convert UUID7 to TypeID format with given prefix."""
    TypeIDCommands.convert_uuid_to_typeid(uuid, prefix)


@cli.command("hex-to-typeid")
@click.argument("hex_value")
@click.argument("prefix")
def hex_to_typeid(hex_value: str, prefix: str) -> None:
    """Convert hexadecimal UUID to TypeID format with given prefix."""
    TypeIDCommands.convert_hex_to_typeid(hex_value, prefix)


@cli.command("hex-to-uuid")
@click.argument("hex_value")
def hex_to_uuid(hex_value: str) -> None:
    """Convert hexadecimal representation to UUID7 format."""
    TypeIDCommands.convert_hex_to_uuid(hex_value)


if __name__ == "__main__":
    cli()