#!/usr/bin/python3
"""Define method file_writing"""


def write_file(filename="", text=""):
    """Write a string
    Args:
        filename:stingb
        text: the text
    Return:
        number of charachters .
    """
    with open(filename, 'w', encoding="UTF-8") as f:
       return f.write(text)
