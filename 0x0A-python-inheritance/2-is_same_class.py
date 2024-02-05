#!/usr/bin/python3
"""Method to check class instance"""


def is_same_class(obj, a_class):
    """Method to check instance

    Args:
        obj: obj.
        a_class: class
    
    Return: true or false.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
