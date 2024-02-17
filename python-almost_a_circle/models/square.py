#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """init the class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    """getter from the attr size"""

    @property
    def size(self):
        return self.width

    """setter from the attr size"""

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    """string method"""

    def __str__(self):
        """return the info of the class"""
        string = f"[Square] ({self.id})"
        string += f" {self.x}/{self.y} - {self.height}"
        return string

    """update the square"""

    def update(self, *args, **kwargs):
        """check if is going to use args or kwargs"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    """convert to dictionary"""

    def to_dictionary(self):
        """create the dictionary"""
        new_dict = {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
        return new_dict
