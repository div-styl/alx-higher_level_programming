#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """revers printing of list numnber"""
    if isinstance(my_list, list):
        for i in reversed(range(len(my_list))):
            print("{}".format(my_list[i]))
