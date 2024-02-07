#!/use/bin/python3
"""Define method to write object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """Function to write ob to text.

       Args:
            my_obj: objext input.
            filename: input file.
       Return:file length
    """
    my_str = json.dumps(my_obj)
    with open(filename, 'w', encoding"UTF-8") as f:
        return f.write(my_str)
