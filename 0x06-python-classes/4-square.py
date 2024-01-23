#!/usr/bin/python3
"""Define class."""


class Square:
    """Define a square."""
    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of a side of square.
        """
        self.size = size

    @property
    def size(self):
        """Property for the length.

        Raises:
            TypeError: if size not int.
            ValueError: if size less than zero.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an intger")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Area of this square.

        Returns:
            The square of size.
        """
        return self.__size ** 2
