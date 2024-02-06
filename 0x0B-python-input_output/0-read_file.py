#!/usr/bin/python3
"""Define text file reading function"""


def read_file(filename=""):
    """Method to read file"""
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end='')
