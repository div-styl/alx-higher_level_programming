#!/usr/bin/python3
"""define a unittest for model/rectangle"""
import unittest

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """class for test the class retangle"""
    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 9), Base)

    def no_arg(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(10)

    def test_two_arg(self):
        r = Rectangle(12, 2)
        r1 = Rectangle(2, 12)
        self.assertEqual(r.id, r1.id)

    def test_as_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 10).__width)

    def test_as_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 10).__height)

    def test_as_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 10).__x)

    def test_as_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 10).__y)

    def test_getter(self):
        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

    def test_setter(self):
        r = Rectangle(10, 10, 10, 10)
        r.width = 20
        r.height = 20
        r.x = 20
        r.y = 20
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 20)
        self.assertEqual(r.y, 20)

    """test the width argumensts"""
    def test_width_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 10)

    def test_width_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integre"):
            Rectangle([1, 2], 4)

    def test_width_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integre"):
            Rectangle({"hey", 2}, 4)

    def test_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integre"):
            Rectangle(float("huh"), 4)

    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 10)

    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 10)

    """test the height argumensts"""
    def test_height_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "10")

    def test_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integre"):
            Rectangle(10, [1, 2])

    def test_height_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integre"):
            Rectangle(10, {"hey", 2})

    def test_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integre"):
            Rectangle(10, float("huh"))

    def test_height_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(-10, 10)

    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)


class TestRectangle_x_and_y(unittest.TestCase):
    """class made to test the x and y"""
    def test_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 10, "10", 10)

    def test_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integre"):
            Rectangle(10, 10, [1, 2], 10)

    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integre"):
            Rectangle(10, 10, {"hey", 2}, 10)

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integre"):
            Rectangle(10, 10, float("huh"), 10)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 10, -10, 10)

    def test_x_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 10, None, 10)

    def test_x_zero(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 10, 0, 10)

    def test_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 10, 10, "10")

    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integre"):
            Rectangle(10, 10, 10, [1, 2])

    def test_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integre"):
            Rectangle(10, 10, 10, {"hey", 2})

    def test_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integre"):
            Rectangle(10, 10, 10, float("huh"))

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 10, 10, -10)

    def test_y_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 10, 10, None)

    def test_y_zero(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 10, 10, 0)

    def test_x_y_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 10, -10, -10)
