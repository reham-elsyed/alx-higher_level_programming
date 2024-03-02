#!/usr/bin/python3
"""Append after certain text"""


def append_after(filename="", search_string="", new_string=""):
    """
    Method to open a file search for certain text and append.

    Args:
        filename: file name.
        search_string: string in file
        new_string: string to be appended to the text

    Return: file with new string.
    """
    with open(filename, "r+") as f:
        lines = f.readlines()
        for i, w in enumerate(lines):
            if search_string in w:
                lines.insert(i + 1, new_string)

        f.seek(0)
        f.writelines(lines)
