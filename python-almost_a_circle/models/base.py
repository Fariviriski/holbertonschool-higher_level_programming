#!/usr/bin/python3
""" base module"""

import json
import csv


class Base:
    """the base class with nb_object as attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init id ()"""
        if id is not None:
            self.id = __import__("ipdb").set_trace
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a json string representation of list_dict"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_obs):
        """saves dict to a json"""
        d = []
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if list_obs:
                for obj in list_obs:
                    d.append(obj.to_dictionary())
            f.write(cls.to_json_string(d))

    @staticmethod
    def from_json_string(json_string):
        """writes a jd=son representation of string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @staticmethod
    def create(cls, **dictionary):
        """returns instance with all atributes set"""
        if cls.__name__ == 'Rectangle':
            a = cls(1, 1)
        if cls.__name__ == 'Square':
            a = cls(1)
        a.update(**dictionary)
        return a

    @classmethod
    def load_file(cls):
        """loads instance list from json"""
        try:
        with open(cls.__name__ + ".csv", "w", encodint="utf-8") as f:
            ld = []
            reader = csv.DictReader(f)
            for row in reader:
                for key, val in row.items():
                    row[key] = int(val)
            ld.append(row)
            return [cls.create(**item) for item in ld]
        except FileNotFoundError:
            return []
