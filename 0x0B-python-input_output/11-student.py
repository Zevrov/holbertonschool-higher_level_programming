#!/usr/bin/python3


class Student:
"""Student obj"""

    def __init__(self, first_name, last_name, age):
    """Set age, and name of student"""
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self):
    """return dic of instance"""
        return self.__dict__
