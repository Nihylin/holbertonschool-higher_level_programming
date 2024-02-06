#!/usr/bin/python3
"""defines a square"""


class Square:
    """I mean this is pretty self explanatory"""

    def __init__(self, size=0, position=(0, 0)):
        """Square class constructor"""
        self.size = size
        self.position = position

    def get_size(self):
        """Size Getter method"""
        return self.__size

    def set_size(self, value):
        """Size Setter method"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def get_position(self):
        """Position Getter method"""
        return self.__position

    def set_position(self, value):
        """Position Setter method"""
        if (
            (type(value) is not tuple or len(value) != 2)
            or
            (type(value[0]) is not int or type(value[1]) is not int)
            or
            (value[0] < 0 or value[1] < 0)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    size = property(get_size, set_size)
    position = property(get_position, set_position)

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character '#'"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
