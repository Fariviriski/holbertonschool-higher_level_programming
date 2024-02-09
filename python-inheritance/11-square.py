#!/usr/bin/python3
"""defines a Rectangle subclass Square"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """represents a Square"""

    def __init__(self, size):
        """initializes a Square based on Rectangle"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
