"""Internal.checks.py

Module for checking variable types and values.
"""


def check_type(
    value: any,
    *expected_types: type,
    raise_exception: bool = True,
    e_type: Exception = TypeError
) -> bool:
    """Checks if the given value is a member of one of the expected types.

    :param value: The value to check.
    :type value: any
    :param expected_types: The type(s) to match with the given value.
    :type expected_type: type
    :param raise_exception: Whether to raise an exception if the check fails.
    :type raise_exception: bool, optional
    :param e_type: The exception to raise if the check fails.
    :type e_type: Exception, optional
    :return: Whether the given value is a member of one of the expected types.
    :rtype: bool
    """

    for expected_type in expected_types:
        if isinstance(value, expected_type):
            return True
    if raise_exception:
        raise e_type(
            f"{value} is not a member of one of the expected types: {expected_types}"
        )
    return False


def check_value(
    value: any,
    *expected_values: any,
    raise_exception: bool = True,
    e_type: Exception = ValueError
) -> bool:
    """Checks if the given value is equal to any of the expected values.

    :param value: The value to check.
    :type value: any
    :param expected_values: The value(s) to match with the given value.
    :type expected_values: any
    :param raise_exception: Whether to raise an exception if the check fails.
    :type raise_exception: bool, optional
    :param e_type: The exception to raise if the check fails.
    :type e_type: Exception, optional
    :return: Whether the given value is equal to one of the expected values.
    :rtype: bool
    """

    for expected_value in expected_values:
        if value == expected_value:
            return True
    if raise_exception:
        raise e_type(
            f"{value} is not equal to one of the expected values: {expected_values}"
        )
    return False


def check_range(
    value: int | float,
    min_value: int | float,
    max_value: int | float,
    raise_exception: bool = True,
    e_type: Exception = ValueError
) -> bool:
    """Checks if the given value is in the range of range(min_value, max_value).

    :param value: The value to check.
    :type value: int | float
    :param min_value: The minimum value of the range.
    :type min_value: int | float
    :param max_value: The maximum value of the range.
    :type max_value: int | float
    :param raise_exception: Whether to raise an exception if the check fails.
    :type raise_exception: bool, optional
    :param e_type: The exception to raise if the check fails.
    :type e_type: Exception, optional
    :return: Whether the given value is in the range.
    :rtype: bool
    """

    in_range = min_value <= value <= max_value
    if not in_range:
        if raise_exception:
            raise e_type(
                f"{value} is not in range({min_value}, {max_value})"
            )
        return False
    return True
