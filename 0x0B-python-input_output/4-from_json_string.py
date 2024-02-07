#!/usr/bin/python3
"""Define method to return obj"""
import json


def from_json_string(my_str):
    """Function to return data

        Args:
            my_str: string

        Return: obj
    """
    return json.loads(my_str)
