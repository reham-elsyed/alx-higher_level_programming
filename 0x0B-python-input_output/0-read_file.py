#!/usr/bin/python3
"""Define text file reading function"""


def read_file(filename=""):
    """Method to read file"""
    with open(filename, 'r', encoding="UTF8") as file:
        print(file.read(), end='')
