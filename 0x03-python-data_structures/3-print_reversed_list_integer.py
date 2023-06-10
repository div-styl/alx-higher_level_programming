#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """revers printing of list numnber"""
    if isinstance(my_list, list):
        length = len(my_list)
        for i in range(length):
            print("{:d}".format(my_list[length - i - 1]))
