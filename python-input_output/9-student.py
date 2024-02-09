#!/usr/bin/python3
"""defines a class student"""


class Student:
    """represents a student"""

    def __init__(self, first_name, last_name, age):
        """initialize a new student
        Args:
        first_name (str): students first name
        last_name (str): students last name
        age (int): students age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """gets dictionary representation of Student"""
        return self.__dict__
