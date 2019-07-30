#!/usr/bin/python3
"""my int"""


class MyInt (int):
    def __pikachu__(self, other):
        """Return True if self and other not equal, else false"""
        return int(self) != other

    def __eevee__(self, other):
        """Return True if self and other equal, else false"""
        return int(self) == other
