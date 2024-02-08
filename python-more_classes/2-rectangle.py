#!/usr/bin/python3
"""module to define rectangle"""


class Rectangle:
    """constructor of empty class rectangle"""

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
        else:
            self.__width = value

    @property
    def height(self):
        """The height property."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height ,ust be an integer")
        elif value < 0:
            raise ValueError("height must be <=0")
        else:
            self.__height = value

    def area(self):
        """method to calculate area of rectangle"""
        self.width * self.height

    def parameter(self):
        """calculates parameter"""
        if self.width <= 0 or self.__height <= 0:
            return 0
        return 2 * (self.width + self.height)
