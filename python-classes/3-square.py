#!/usr/bin/python3
"""Square module."""


class Square:
    """initialize instance attributes methods"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.size = size

    def area(self):
        return self.size * self.size
