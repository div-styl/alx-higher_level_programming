#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """revers printing of list numnber"""
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print('{:d}'.format(i))

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
