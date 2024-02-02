#!/usr/bin/python3
"""
unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TextMaxInteger(unittest.TestCase):
    """max_integer tests"""
    def setup(self):
        self.ordred_list = [1, 2, 3, 4]
        slef.unordered_list = [4, 2, 1, 3]

    def tesr_mxs(self):
        delf.assertEqual(max_integer(self.ordred_list),
                         max_integer(self.unordered_list))

    def test_str(self):
        self.assertEqual(max_integer("string"), 't')

    def test_none(self):
        self.assertEqual(max_integer(), None)

    def test_list_negatives(self):
        with self.assertEqual(max_integer([-420, -69, -97]), -1)

    def test_ky_err(self):
        with self.assertRaises(KeyError):
            max_integer({5 : 6})

    def test_2many_args(self):
        with self.assertRaises(TypeError):
            max_integer('tuple', 'strings')

    def test_incompatible_items(self):
        with self.assertRaises(TypeError):
            max_integer([[], {}])
