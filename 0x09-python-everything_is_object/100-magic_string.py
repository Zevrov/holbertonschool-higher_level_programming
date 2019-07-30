#!/usr/bin/python3
def magic_string():
    setattr(magic_string, "x", getattr(magic_string, "x", -1) + 1)
    ret = ("Holberton" + ", Holberton" * getattr(magic_string, "x", 0))
    return ret
