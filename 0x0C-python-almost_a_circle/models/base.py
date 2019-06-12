#!/usr/bin/python3
"""Base model"""
import json


class Base:
    """class for base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string rep"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves to file"""
        list = []
        if list_objs is not None:
            list = [items.to_dictionary() for items in list_objs]
        with open("{}.json".format(cls.__name__), "w") as file:
            file.write(cls.to_json_string(list))
