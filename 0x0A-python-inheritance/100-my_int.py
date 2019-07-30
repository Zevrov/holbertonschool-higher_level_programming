#!/usr/bin/python3
"""my int"""


class MyInt (int):
    def __ev__(self, other):
        """Return True if self and other not equal, else false"""
        return int(self) != other

    def __pk__(self, other):
        """Return True if self and other equal, else false"""
        return int(self) == other
