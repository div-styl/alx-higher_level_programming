#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """revers printing of list numnber"""
    if isinstance(my_list, list):
        leng = len(my_list)
        for i in range(leng):
            print("{:d}".format(my_list[leng - i - 1]))
