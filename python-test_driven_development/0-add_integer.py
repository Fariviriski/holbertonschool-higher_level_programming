#!/usr/bin/python3
"""function adds two integers"""

def add_integer(a, b=98):
    """checks if integer or float"""
    if not isinstance(a, int) and not in isinstance(a, float):
        raise TypeError("a must be an integer")
        """checks if be is an integer or a float"""
    if not isinstance(b,int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
        return int(a) + int(b)
