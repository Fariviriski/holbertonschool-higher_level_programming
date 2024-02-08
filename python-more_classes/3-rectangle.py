#!/usr/bin/python3
"""module for rectangle class"""


class Rectangle:
    """constructor of rectangle class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """The width property."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The height property."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an int")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        "method for area calc"
        return self.width * self.height

    def perimeter(self):
        "method for perimeter calc"
        if self.__width <= 0 or self.__height <= 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """prints rectangle to stdout"""
        result = ""
        if self.width <= 0 or self.height <= 0:
            return result
        else:
            for h in range(self.height):
                for w in range(self.width):
                    result += "#"
                if h != (self.height - 1):
                    result = result + "\n"
        return result
