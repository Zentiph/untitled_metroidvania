"""Internal.interp.py

Contains functions used to interpolate movement.
"""

from math import cos as __cos
from math import pi as __pi
from math import pow as __pow
from math import sin as __sin
from math import sqrt as __sqrt

from .checks import check_range as __check_range
from .checks import check_type as __check_type


def lerp(
    start: int | float,
    end: int | float,
    t: int | float
) -> int | float:
    """Linear interpolation function.

    :param start: The starting value.
    :type start: int | float
    :param end: The ending value.
    :type end: int | float
    :param t: The interpolation t (0 <= t <= 1).
    :type t: int | float
    :return: The interpolated value.
    :rtype: float
    """

    __check_type(start, int, float)
    __check_type(end, int, float)
    __check_type(t, int, float)
    __check_range(t, 0, 1)

    return start + t * (end - start)


def linear(t: int | float) -> int | float:
    return t


def ease_in_sine(t: int | float) -> int | float:
    return -__cos(t * __pi / 2) + 1


def ease_out_sine(t: int | float) -> int | float:
    return __sin(t * __pi / 2)


def ease_in_out_sine(t: int | float) -> int | float:
    return -(__cos(__pi * t) - 1) / 2


def ease_in_quad(t: int | float) -> int | float:
    return t * t


def ease_out_quad(t: int | float) -> int | float:
    return -t * (t - 2)


def ease_in_out_quad(t: int | float) -> int | float:
    t *= 2
    if t < 1:
        return t * t / 2
    t -= 1
    return -(t * (t - 2) - 1) / 2


def ease_in_cubic(t: int | float) -> int | float:
    return t * t * t


def ease_out_cubic(t: int | float) -> int | float:
    t -= 1
    return t * t * t + 1


def ease_in_out_cubic(t: int | float) -> int | float:
    t *= 2
    if t < 1:
        return t * t * t / 2
    t -= 2
    return (t * t * t + 2) / 2


def ease_in_quart(t: int | float) -> int | float:
    return t * t * t * t


def ease_out_quart(t: int | float) -> int | float:
    t -= 1
    return -(t * t * t * t - 1)


def ease_in_out_quart(t: int | float) -> int | float:
    t *= 2
    if t < 1:
        return t * t * t * t / 2
    t -= 2
    return -(t * t * t * t - 2) / 2


def ease_in_quint(t: int | float) -> int | float:
    return t * t * t * t * t


def ease_out_quint(t):
    t -= 1
    return t * t * t * t * t + 1


def ease_in_out_quint(t):
    t *= 2
    if t < 1:
        return t * t * t * t * t / 2
    t -= 2
    return (t * t * t * t * t + 2) / 2


def ease_in_exp(t):
    return __pow(2, 10 * (t - 1))


def ease_out_exp(t):
    return -__pow(2, -10 * t) + 1


def ease_in_out_exp(t):
    """Scary! Might cause an exception.
    """
    t *= 2
    if t < 1:
        return __pow(2, 10 * (t - 1)) / 2
    t -= 1
    return -__pow(2, -10 * t) - 1


def ease_in_circ(t):
    return 1 - __sqrt(1 - t * t)


def ease_out_circ(t):
    t -= 1
    return __sqrt(1 - t * t)


def ease_in_out_circ(t):
    t *= 2
    if t < 1:
        return -(__sqrt(1 - t * t) - 1) / 2
    t -= 2
    return (__sqrt(1 - t * t) + 1) / 2
