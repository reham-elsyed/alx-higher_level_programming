#!/usr/bin/python3
"""Define class"""
from json import dumps, loads


class Base:
    """Class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """stringfy data"""
        if list_dictionaries in None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)
