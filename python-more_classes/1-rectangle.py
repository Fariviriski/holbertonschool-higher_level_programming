#!/usr/bin/python3
"""
module that defines Rectangle class
"""


class Rectangle:
    "defines a rectangle with area"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """The width property."""
        return self.__width

    @property
    def height(self):
        """The height property."""
        return self.__height

    @width.setter
    def width(self, value):
        """sets the width value of a rectangle"""
        if isnotinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        return self.__width

    @height.setter
    def height(self, value):
        """sets height value of a rectangle"""
        if isnotinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        return self.__height
