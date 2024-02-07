#!/usr/bin/python3
"""Function to create an object"""
import json


def load_from_json_file(filename):
    """Function to return

    Args:
        filename: file name.
    """
    with open(filename, 'r') as f:
        obj = f.read()
        return json.loads(obj)
