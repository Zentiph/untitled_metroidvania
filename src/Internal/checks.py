"""Internal.checks.py

Module for checking variable types and values.
"""


def check_type(
    value: any,
    *expected_types: type
) -> bool:
    """Checks that the given value is a member of one of the expected types.

    :param value: The value to check.
    :type value: any
    :param expected_types: The type(s) to match with the given value.
    :type expected_type: type
    :return: Whether the given value is a member of one of the expected types.
    :rtype: bool
    """

    for expected_type in expected_types:
        if isinstance(value, expected_type):
            return True
    return False
