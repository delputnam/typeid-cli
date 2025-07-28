"""ID conversion utilities for handling UUID and TypeID formats."""

from uuid import UUID

from typeid import TypeID


def typeid_to_uuid7(typeid_str: str) -> str:
    """
    Convert a TypeID to its UUID7 representation.

    Args:
        typeid_str: TypeID string like 'contact_01k0g0hzrsed3scjp07tsz36y8'

    Returns:
        UUID7 string like '01234567-89ab-cdef-0123-456789abcdef'

    Raises:
        ValueError: If the TypeID format is invalid
    """
    try:
        typeid = TypeID.from_string(typeid_str)
        uuid_obj = typeid.uuid
        return str(uuid_obj)
    except Exception as e:
        raise ValueError(f"Failed to convert TypeID '{typeid_str}' to UUID: {e}")


def uuid7_to_typeid(uuid_str: str, prefix: str) -> str:
    """
    Convert a UUID7 to TypeID format with the given prefix.

    Args:
        uuid_str: UUID string like '01234567-89ab-cdef-0123-456789abcdef'
        prefix: TypeID prefix like 'contact' or 'user_notification'

    Returns:
        TypeID string like 'contact_01k0g0hzrsed3scjp07tsz36y8'

    Raises:
        ValueError: If the UUID format is invalid
    """
    try:
        uuid_obj = UUID(uuid_str)
        typeid = TypeID.from_uuid(uuid_obj, prefix=prefix)
        return str(typeid)
    except Exception as e:
        raise ValueError(f"Failed to convert UUID '{uuid_str}' to TypeID with prefix '{prefix}': {e}")


def hex_to_typeid(hex_str: str, prefix: str) -> str:
    """
    Convert a hexadecimal UUID representation to TypeID format.

    Args:
        hex_str: Hex string like '0x01977609240070008000000000000000' or '01977609240070008000000000000000'
        prefix: TypeID prefix like 'contact' or 'user_notification'

    Returns:
        TypeID string like 'contact_01k0g0hzrsed3scjp07tsz36y8'

    Raises:
        ValueError: If the hex format is invalid
    """
    try:
        hex_str = hex_str.removeprefix("0x")

        if len(hex_str) != 32:
            raise ValueError(f"Hex string must be exactly 32 characters (128 bits), got {len(hex_str)}")

        uuid_bytes = bytes.fromhex(hex_str)
        uuid_obj = UUID(bytes=uuid_bytes)
        typeid = TypeID.from_uuid(uuid_obj, prefix=prefix)
        return str(typeid)
    except Exception as e:
        raise ValueError(f"Failed to convert hex '{hex_str}' to TypeID with prefix '{prefix}': {e}")


def hex_to_uuid7(hex_str: str) -> str:
    """
    Convert a hexadecimal representation to UUID7 format.

    Args:
        hex_str: Hex string like '0x01977609240070008000000000000000' or '01977609240070008000000000000000'

    Returns:
        UUID7 string like '01977609-2400-7000-8000-000000000000'

    Raises:
        ValueError: If the hex format is invalid
    """
    try:
        hex_str = hex_str.removeprefix("0x")

        if len(hex_str) != 32:
            raise ValueError(f"Hex string must be exactly 32 characters (128 bits), got {len(hex_str)}")

        uuid_bytes = bytes.fromhex(hex_str)
        uuid_obj = UUID(bytes=uuid_bytes)
        return str(uuid_obj)
    except Exception as e:
        raise ValueError(f"Failed to convert hex '{hex_str}' to UUID: {e}")


def generate_new_typeid(prefix: str) -> tuple[str, str]:
    """
    Generate a new TypeID with the given prefix.

    Args:
        prefix: TypeID prefix like 'user' or 'contact'

    Returns:
        Tuple of (typeid_string, uuid_string)

    Raises:
        ValueError: If the prefix is invalid
    """
    try:
        typeid = TypeID(prefix=prefix)
        return str(typeid), str(typeid.uuid)
    except Exception as e:
        raise ValueError(f"Failed to generate TypeID with prefix '{prefix}': {e}")
