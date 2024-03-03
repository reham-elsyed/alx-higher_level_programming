i#!/usr/bin/python3
"""
Method to checlinstance of a class that inherited (directly or indirectly)
"""


def inherits_from(obj, a_class):
    """Method to check inheritance"""
    if isinstance(a_class, obj):
        return True
    else:
        return False
