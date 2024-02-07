#!/use/bin/python3
"""Add all args in a python list and save them"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

arg_data = sys.argv[1:]

try:
    data = load_from_json_file('add_item.json')
except FileNoteFoundError:
    data = []

    data.extend(data_arg)
    save_to_json_file(data, 'add_item.json')
