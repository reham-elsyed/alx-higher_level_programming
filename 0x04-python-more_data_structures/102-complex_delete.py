#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    else:
        key_del = [key for key, val in a_dictionary.items() if val == value]
        for key in key_del:
            del a_dictionary[key]
        return a_dictionary
