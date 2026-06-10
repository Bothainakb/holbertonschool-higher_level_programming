#!/usr/bin/python3
"""This module provides a function that divides all elements of a matrix.

The function validates the matrix and divisor before returning
a new matrix with each element divided and rounded to 2 decimals.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a number.

    Returns a new matrix with elements rounded to 2 decimal places.
    Raises exceptions for invalid matrices or divisors.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(error_msg)

    row_length = len(matrix[0])

    for row in matrix:
        if len(row) != row_length:
            raise TypeError(
                "Each row of the matrix must have the same size"
            )

        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError(error_msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(value / div, 2) for value in row] for row in matrix]
