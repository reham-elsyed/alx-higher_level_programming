#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic_t = sorted(a_dictionary)
    for i in dic_t:
        print("{}:{}".format(i, a_dictionary[i]))
