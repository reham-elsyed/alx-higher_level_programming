#!/usr/bin/python3
"""Define class"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print sorted self"""
        print(sorted(self))
