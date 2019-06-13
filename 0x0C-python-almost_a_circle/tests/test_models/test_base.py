#!/usr/bin/python3
"""Unittests for base model"""
import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testbase(unittest.TestCase):
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

    def test_docstring(self):
        """test docstring"""
        self.assertIsNotNone(Base.__doc__)

    def Nargs(self):
        """testing for no arguments"""
        x = Base()
        x = self.assertEqual(x.id, 1)

    def Margs(self):
        """testing too many arguments"""
        x = Base()
        self.assertEqual(x.id, 1)
        self.assertRaises(TypeError, Base, 23, 43)
        x = Base()
        self.assertEqual(b.id, 2)

    def json(self):
        """json test"""
        x = Base()
        self.assertEqual(x.id, 1)

    def id(self):
        """test for id"""
        x = Base()
        self.assertEqual(x.id, 1)
        y = Base(14)
        self.assertEqual(y.id, 14)
        z = Base()
        self.assertEqual(z.id, 2)
