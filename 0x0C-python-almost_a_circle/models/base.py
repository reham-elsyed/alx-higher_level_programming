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

    @staticmethod
    def to_json_string(list_dictionaries):
        """stringfy data"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """String representaion"""
        if list_objs is None:
            list_objs = [i.to_dictionary() for i in list_objs]
        else:
            with open(f"{cls.__name__}.json", "w", encoding="UTF-8") as f:
                f.write(cls.to_json_string(list_objs))
