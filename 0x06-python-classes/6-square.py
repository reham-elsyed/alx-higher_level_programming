#!/usr/bin/python3
"""Define class."""


class Square:
    """Define square."""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor.

        Args:
            size: length of a side of square.
            position: position of square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Property for length.

        Raise:
            TypeError: if sizr not ingtger.
            ValueError: if size less than zero.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Property for length.

            Raise:
                TypeError: if sizr not ingtger.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for element in value:
            if not isinstance(element, int) or element < 0:
                raise TypeError("position must be ", end="")
                raise TypeError("a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area of this square.

        Returns:
            the size squae.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints of this squar."""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for m in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
