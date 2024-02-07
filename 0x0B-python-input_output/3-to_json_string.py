#!/usr/bin/python3
"""Define method to stringfy json"""
import json


def to_json_string(my_obj):
    """Function to string json

    Args:
        my_obj: object

    Return:
        json rep of object
    """
    return json.dumps(my_obj)
