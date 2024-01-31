#!/usr/bin/python3
"""Define class"""


class Rectangle:
    """Class rectangle"""
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """Constructor.

        Args:
            width: width.
            height: height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        result = ""
        result += '\n'.join(["#" * self.__width for i in range(self.__height)])
        return result

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height}"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
