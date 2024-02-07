#!/usr/bin/python3
"""Define class"""


class Student:
    """Class student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method to retrive dictionary representation"""
        new_dict = {}
        new_att = vars(self)

        for key, value in new_att.items():
            if isinstance(value, (list, int, str, dict)):
                new_dict[key] = value
        return new_dict
