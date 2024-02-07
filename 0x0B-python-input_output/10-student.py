#!/usr/bin/python3
"""Define class"""


class Student:
    """Class define student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:

            attrs = vars(self).keys()
        else:
            attrs = [attr for attr in attrs if hasattr(self, attr)]
        return {attr: getattr(self, attr) for attr in attrs}
