#!/usr/bin/python3
"""defines basic geometry class BaseGeometry"""

class BaseGeometry:
    """BaseGeometry"""
     def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator
        Args:
        Returns:
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))
