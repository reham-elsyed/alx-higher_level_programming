#!/usr/bin/python3
"""Define fnction for serialization"""


def class_to_json(obj):
    """Function to serialize

    Args:
        odj: object
    Return: dictionary
    """
    new_dict = {}
    obj_att = vars(obj)
    for key, value in obj_att.items():
        if isinstance(value, (list, int, str, bool, dict)):
            new_dict[key] = value
    return new_dict
