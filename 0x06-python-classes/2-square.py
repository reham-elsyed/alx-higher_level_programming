#!/usr/bin/python3
""" Define class."""
class Square:
    """ Define suare."""

    def __init__(self, size=0):
        """
        Constri=uctor.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
