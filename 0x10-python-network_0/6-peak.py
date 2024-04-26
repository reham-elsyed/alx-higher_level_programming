#!/usr/bin/python3
""" Method to find peak in an unsorted list"""


def find_peak(list_of_integers):
    """ Find peak in a list of integers"""
    if len(list_of_integers) == 0:
        return None
    else:
        peak = 0
        for i, num in enumerate(list_of_integers):
            peak = num
            if i < len(list_of_integers) - 1 and \
                num > list_of_integers[i + 1] and \
                    num > list_of_integers[i - 1]:
                return num
        return peak
