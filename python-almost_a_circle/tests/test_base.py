#!/usr/bin/python3
"""unittest for base model"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class BaseTest(unittest.TestCase):
    "unittest class for base tests"

    def set_tha_zero(self):
        "sets base instance counter to zero"
        Base._Base__nb_objects = 0

    def test1(self):
        """test basic function of Base class"""
        b = Base(1)
        self.assertTrue(type(b) is Base)

    def test2(self):
        """test id of base"""
        self.set_tha_zero()
        b = Base()
        b2 = Base()
        b3 = Base(69)
        b4 = Base()
        self.assertEqual(b.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 69)
        self.assertEqual(b4.id, 3)

    def test2_1(self):
        """more id shenanigans"""
        self.set_tha_zero()
        b = Base(-1)
        b2 = Base(0)
        b3 = Base()
        self.assertEqual(b.id, -1)
        self.assertEqual(b2.id, 0)
        self.assertEqual(b3.id, 1)

    def test3(self):
        """testing json to string"""
        self.set_tha_zero()
        r = Rectangle(10, 7, 2, 8)
        r_dict = r.to_dictionary()
        json_dicti = Base.to_json_string([r_dict])
        self.assertTrue(type(r_dict) is dict)
        self.assertTrue(type(json_dicti) is str)
        self.assertEqual(
            json_dicti,
            '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]',
        )

    def test3_1(self):
        """more json to str shenanigans"""
        json_dicti = Base.to_json_string([])
        self.assertTrue(type(json_dicti) is str)
        self.assertEqual(json_dicti, "[]")

    def test3_2(self):
        """even moar json but with rectangle"""
        self.set_tha_zero()
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6, 7, 8)
        r1, r2 = r1.to_dictionary(), r2.to_dictionary()
        json_dicti = Base.to_json_string([r1, r2])
        self.assertTrue(type(json_dicti) is str)
        self.assertEqual(
            json_dicti,
            '[{"x": 3, "y": 4, "id": 1,\
 "height": 2, "width": 1}, {"x": 7, "y": 8, "id":\
 2, "height": 6, "width": 5}]',
        )

    def test4(self):
        """testing from json string"""
        list_input = [
            {"id": 69, "width": 10, "height": 9},
            {"id": 420, "width": 1, "height": 2},
        ]
        json_dicti = Base.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_dicti)
        self.assertTrue(type(list_input) is list)
        self.assertTrue(type(json_dicti) is str)
        self.assertEqual(
            json_dicti,
            '[{"id": 69, "width": 10, \
"height": 9}, {"id": 420, "width": 1, "height": 2}]',
        )

    def test4_1(self):
        """mor from_json_string"""
        list_input = None
        output = Base.from_json_string(list_input)
        self.assertEqual(output, [])

    def test4_2(self):
        """evan moar from_json_string"""
        list_input = []
        json_dicti = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_dicti)
        self.assertEqual(list_output, [])

    def test5(self):
        """dict to isntance"""
        self.set_tha_zero()
        r1 = Rectangle(1, 2, 3)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 3/0 - 1/2")

    def test5_1(self):
        """dict to instance 2, the instancing"""
        self.set_tha_zero()
        s1 = Square(1, 2, 3)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(s1.__str__(), "[Square] (1) 2/3 - 1")

    def test6(self):
        """test load_from_file"""
        self.set_tha_zero()
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6)
        list_input = [r1, r2]
        Rectangle.save_to_file(list_input)
        if os.path.exists("Rectangle.json"):
            list_output = Rectangle.load_from_file()
            for i, rect in enumerate(list_output):
                self.assertTrue(type(rect) is Rectangle)
                self.assertEqual(rect.__str__(), list_input[i].__str__())
            os.remove("Rectangle.json")

    def test6_1(self):
        """more load_from_file"""
        self.set_tha_zero()
        s1 = Square(1, 2, 3, 4)
        s2 = Square(5, 6)
        list_input = [s1, s2]
        Square.save_to_file(list_input)
        if os.path.exists("Square.json"):
            list_output = Square.load_from_file()
            for i, sq in enumerate(list_output):
                self.assertTrue(type(sq) is Square)
                self.assertEqual(sq.__str__(), list_input[i].__str__())
            os.remove("Square.json")

    def test6_2(self):
        """load_from_file 3, loadmegaladon"""
        list_output = Rectangle.load_from_file()
        self.assertEqual(list_output, [])

    def test6_3(self):
        """load_from_file 4, the forthcoming"""
        list_output = Square.load_from_file()
        self.assertEqual(list_output, [])
