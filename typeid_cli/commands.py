"""Command implementations for TypeID CLI."""

import sys

from .id_utils import hex_to_typeid, hex_to_uuid7, typeid_to_uuid7, uuid7_to_typeid


class TypeIDCommands:
    """Commands for TypeID conversions."""

    @staticmethod
    def convert_typeid_to_uuid(typeid_str: str) -> None:
        """Convert TypeID to UUID7 format."""
        try:
            uuid_result = typeid_to_uuid7(typeid_str)
            print(uuid_result)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    @staticmethod
    def convert_uuid_to_typeid(uuid_str: str, prefix: str) -> None:
        """Convert UUID7 to TypeID format with given prefix."""
        try:
            typeid_result = uuid7_to_typeid(uuid_str, prefix)
            print(typeid_result)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    @staticmethod
    def convert_hex_to_typeid(hex_str: str, prefix: str) -> None:
        """Convert hexadecimal UUID to TypeID format with given prefix."""
        try:
            typeid_result = hex_to_typeid(hex_str, prefix)
            print(typeid_result)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    @staticmethod
    def convert_hex_to_uuid(hex_str: str) -> None:
        """Convert hexadecimal representation to UUID7 format."""
        try:
            uuid_result = hex_to_uuid7(hex_str)
            print(uuid_result)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)