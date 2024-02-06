#!/usr/bin/python3
"""defines a square"""


class Square:
    """I mean this is pretty self explanatory"""

    def __init__(self, size=0):
        """Square class constructor"""
        self.__size = size

    def get_size(self):
        """Getter method"""
        return self.__size

    def set_size(self, value):
        """Setter method"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    size = property(get_size, set_size)

    def my_print(self):
        """prints in stdout the square with the character '#'"""
        if self.__size == 0:
            print()
        else:
            for idx in range(self.__size):
                print("#" * self.__size)
