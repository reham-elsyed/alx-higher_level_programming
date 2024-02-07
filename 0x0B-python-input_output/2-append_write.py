#!/usr/bin/python3
"""Method to write to file"""


def append_write(filename="", text=""):
    """Function to append text to file.

    Args:
        filename: file
        text: text to be appended.
    Return:
        length of text
    """
    with open(filename, 'a', encoding="UTF-8") as f:
        return f.write(text)
