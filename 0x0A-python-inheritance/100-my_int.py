#!/usr/bin/python3
"""my int"""


class MyInt (int):
    def __nequal__(self, other):
        """Return True if self and other not equal, else false"""
        return int(self) != other

    def __equal__(self, other):
        """Return True if self and other equal, else false"""
        return int(self) == other
