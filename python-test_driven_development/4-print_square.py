#!/usr/bin/python3
"""
module that defines print_square
"""

def print_square(size):
    """
    prints a square with the '#' character
    Args: size(int)
    """
    if not isinstance(size, int):
        raise TypeError("size must be an int")

    if size < 0:
        raise ValueError("size must me >= 0")


    for i in range(size):
        print("#" * size)
