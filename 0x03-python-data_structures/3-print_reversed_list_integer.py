#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """revers printing of list numnber"""
    for i in range(len(my_list) - 1, -1, -1):
        print('{}'.format(my_list[i]))
