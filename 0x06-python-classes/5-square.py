#!/usr/bin/python3
"""Define class"""


class Square:
    """Define square"""
    def __init__(self, size=0):
        """Constructor.

        Args:
            size: length of a side of square.
        """
        self.__size = size

    @property
    def size(self):
        """Property for length.

        Raise:
            TypeError: if sizr not ingtger.
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
        """Area of this square.

        Returns:
            the size squae.
        """
        current_square_area = self.__size ** 2
        return current_square_area

    def my_print(self):
        """prints this square."""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for row in range(self.size):
                    print("#", end="")
                print()
