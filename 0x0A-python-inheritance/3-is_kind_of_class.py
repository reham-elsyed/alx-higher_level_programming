#!/usr/bin/python3
"""
Method to check  the object is an instance of,
or if the object is an instance of a class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """Check if element is instance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
