#!/usr/bin/python3
"""Square module."""

class Square:
    """initialize instance attributes methods"""
    def __init__(self, size=0):
            TypeError: if size is not an integer
            ValueError: if size < 0
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("value must be >= 0")
        self.__size = size

        def area(self):
            return self.__size ** 2
