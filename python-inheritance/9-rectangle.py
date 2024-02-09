#!/usr/bin/python3
"""class rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """represents rectangle with BaseGeometry"""

    def __init__(self, width, height):
        """__init__ rectangle"""

        supper().integer_validator("width", width)
        self.__width = width
        supper().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """reutrns print and sr representation of rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
