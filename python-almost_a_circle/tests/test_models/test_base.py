#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        # Test case for id = 0 should raise ValueError
        with self.assertRaises(ValueError):
            Base.validate_id(0)


if __name__ == "__main__":
    unittest.main()
