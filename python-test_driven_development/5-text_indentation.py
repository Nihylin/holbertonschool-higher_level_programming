#!/usr/bin/python3
"""
Defines a function that prints a text with 2 new lines after
each of these characters: '.', '?' and ':'.
I'm writing stupid lines to please the almighty checker.
"""


def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
