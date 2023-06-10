#!/usr/bin/python3
def max_integer(my_list=[]):
    """return the largest value with in the list"""
    largest_value = None
    len_list = len(my_list)
    if len_list < 0:
        return (None)
    for i in my_list:
        if largest_value is None or largest_value < i:
            largest_value = i
    return (largest_value)
