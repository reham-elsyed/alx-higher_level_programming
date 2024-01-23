#!/usr/bin/python3
""" Define class."""
class Square:
    """ Define suare."""

    def __init__(self, size=0):
        """
        Constri=uctor.
        """
        self.size = size

    @size.setter
    def size(self, value):
        if value.isdigit():
            self.__size = value
            raise TypeError("size must be an integer")
        else:
            if value < 0:
            raise TypeError("size must be >= 0")
