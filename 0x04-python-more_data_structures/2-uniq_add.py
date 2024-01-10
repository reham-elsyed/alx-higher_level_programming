#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = my_list.copy()
    new_list = list(set(new_list))
    new_list.sort()
    sum = 0
    for i in range(len(new_list) + 1):
        sum += i
    return sum
