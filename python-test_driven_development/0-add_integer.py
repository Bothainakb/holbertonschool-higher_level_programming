#!/usr/bin/python3
"""This module provides a function that adds two integers.

The function validates the arguments before performing the addition.
It converts float values to integers before calculating the result.
"""


def add_integer(a, b=98):
    """Return the sum of two integers.

    Float arguments are converted to integers before addition.
    Raises TypeError if either argument is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
