#!/usr/bin/python3
"""
defines a rectangle
"""


class Rectangle:
    """defines a rectangle by width and height"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Rectangle class constructor"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    @property
    def width(self):
        """Get the width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        row = str(self.print_symbol) * self.width
        rect = row
        for i in range(self.height - 1):
            rect += "\n" + row
        return rect

    def __repr__(self):
        """"Return a string representation of rectangle instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
