#!/usr/bin/python3
"""Module for add_intger method"""


def add_integer(a, b=98):
    """Adds two ints;

    Args:
        a: first int.
        b:second int. default 98.

    Raises:
        TypeError: if args not int.

    Returns:
        The sum of the two ints.
    """

    if not isinstance(a, int):
        if isinstance(a, float):
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if not isinstance(b, int):
        if isinstance(b, float):
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b;

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
