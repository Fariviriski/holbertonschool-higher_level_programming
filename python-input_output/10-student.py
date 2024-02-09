#!/usr/bin/python3
"""defines a class Student"""


class Student:
    """represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Student to json.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            retun {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
