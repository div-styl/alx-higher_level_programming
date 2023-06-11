#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """print element within a list"""
    if my_list is None:
        return (my_list)
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
