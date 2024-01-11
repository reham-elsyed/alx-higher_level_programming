#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    sorted_dict = {k: a_dictionary[k] for k in sorted_keys}
    print(sorted_dict)
