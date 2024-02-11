#!/usr/bin/python3
"""
Defines a function that divides all elements of a matrix.
I'm writing stupid lines to please the almighty checker.
This is ABSURD.
"""


def matrix_divided(matrix, div):
    """
    Division of all elements of a matrix.
    """

    if not all(
                isinstance(row, list) and
                all(isinstance(elem, (int, float)) for elem in row)
                for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_sizes = [len(row) for row in matrix]
    if len(set(row_sizes)) > 1:
        raise TypeError(
            "Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
