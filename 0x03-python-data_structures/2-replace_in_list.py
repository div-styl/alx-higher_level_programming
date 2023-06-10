#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """a function that replaces an element of a list at a specific position"""
    len_list = len(my_list)
    if idx >= 0 or idx < len_list:
        my_list[idx] = element
    return (my_list)
