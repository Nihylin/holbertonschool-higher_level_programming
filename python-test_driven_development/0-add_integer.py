#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Addition of two variables"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return int(a + b)
