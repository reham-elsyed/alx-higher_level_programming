#!/usr/bin/python3
""" Define class."""


class Square:
    """ Define suare."""

    def __init__(self, size=0):
        """
        Constructor.

        Args:
            size: length.

        Raises:
            TypeError: if not intger
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area if this square.

        Return:
        The size squared'
        """
        return self.__size ** 2
