#!/usr/bin/python3
"""
Defines a function that prints 'My name is <first name> <last name>'
I'm writing stupid lines to please the almighty checker.
This is ABSURD.
"""


def say_my_name(first_name, last_name=""):
    """
    Printing of a name.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
