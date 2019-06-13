#!/usr/bin/python3
"""tests made for rectangles"""


import unittest
import contextlib
import importlib
import io
import models.base
import models.rectangle


Rect = models.rectangle.Rectangle


class rectangle_tests(unittest.TestCase):
    """yay, rectangle testing"""
    def setUp(self):
        """refresh for each test"""
        importlib.reload(models.base)
        importlib.reload(models.rectangle)

    def test_TooFewArgs(self):
        """Test for too few args to init"""
        err = "missing heigt arg fool"
        with self.assertRaises(TypeError, msg=err):
            Rect(1)

    def def test_TooManyArgs(self):
        """Test for too many args to init"""
        err = "too many arguments man"
        with self.assertRaises(TypeError, msg=err):
            Rect(1, 1, 1, 1, 1, 1)

    def test_Area(self):
        """Compare width and height to result of area method"""
        testrect = Rect(7, 6)
        with self.subTest():
            self.assertEqual(testrect.area(), 42)
        testrect.width = 4
        testrect.height = 5
        with self.subTest():
        self.assertEqual(testrect.area(), 20)
