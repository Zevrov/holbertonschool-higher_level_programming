#!/usr/bin/python3
"""Unittests for base model"""
import unittest
from models.base import Base


class test_base(unittest.TestCase):
    """unit testing"""
    def setup(self):
        """setup"""
        importlib.reload(models.Base)
        importlib.reload(models.Rectangle)
        importlib.reload(models.Square)

    def None(self):
        """testing for no input"""
        x = Base(None)
        y = Base()
        self.assertEqual(x.id, 1)
        self.assertEqual(y.id, 2)

    def Nargs(self):
        """testing for no arguments"""
        x = Base()
        x = self.assertEqual(x.id, 1)
