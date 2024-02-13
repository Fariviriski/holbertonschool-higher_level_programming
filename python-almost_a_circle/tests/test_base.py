#!/usr/bin/python3
"""defines unittest for base.py"""

import unittest
import json
from models import Base

Base = base.base


class TestBase(unittest.TestCase):
    """checks for base class"""

    def too_many_args(self):
        """testing for cuantity of args"""
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def no_id(self):
        """testing id as none"""
        b = base()
        self.assertEqual(b.id, 1)

    def id_set(self):
        """test for id as not none"""
        b98 = base(98)
        self.assertEqual(b98.id, 98)

    def no_id_aftr_set(self):
        """testing id set to None after not None"""
        b2 = base()
        self.assertEqual(b2.id, 2)

    def nb_private(self):
        """testing nb objects as private instance"""
        b = base(3)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def to_json_string(self):
        """testing to json string"""
        Base._Base__nb_objects = 0
        d1 = {"id": 69, "width": 15, "height": 42, "x": 7, "y": 9}
        d2 = {"id": 3, "width": 4, "height": 2, "x": 6, "y": 8}
        json_s = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_s) is str)
        d = json.loads(json_s)
        self.assertEqual(json_s, "[]")

    def from_json_string(self):
        """tests from json string"""
        json_str = '[{"id": 69, "width": 15, "height": 42, "x": 7, "y": 9} , \
        {"id": 3, "width": 4, "height": 2, "x": 6, "y": 8}]'
        json_1 = BAse.from_json_string(jason_str)
        self.assertTrue(type(json_1) is list)
        self.assertEqual(len(json_1), 2)
        self.assertEqual(type(json_1[0]) is dict)
        self.assertEqual(type(json_1[1]) is dict)
        self.assertEqual(
            json_1[0], {"id": 69, "width": 15, "height": 42, "x": 7, "y": 9}
        )
        self.assertEqual(json_1[1], {"id": 3, "width": 4, "height": 2, "x": 6, "y": 8})

    def frmjson_empty(self):
        """tests from_json_string with empty str"""
        self.assertEqual([], Base.from_json_string(""))

    def frmjson_None(self):
        """testing with a None String"""
        self.assertEqual({}, Base.from_json_string(None))
