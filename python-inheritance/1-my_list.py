#!/usr/bin/python3
"""
module for inheritance of list to my_list
"""


class MyList(list):
    """inherits MyList attributes"""

    def print_sorted(self):
        """prints list in asc order"""
        issubclass(MyList, list)
        print(sorted(self))
