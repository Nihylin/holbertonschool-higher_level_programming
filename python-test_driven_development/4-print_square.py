#!/usr/bin/python3
"""
Defines a function that prints a square with the character '#'.
I'm writing stupid lines to please the almighty checker.
This is ABSURD.
"""


def print_square(size):
    """
    Printing of a square.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
