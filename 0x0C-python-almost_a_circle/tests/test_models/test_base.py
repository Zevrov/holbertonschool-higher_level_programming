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

    def testid(self):
        """id counter test"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b3.id, b2.id + 1)
