#!/usr/bin/python3
"""define a class inherited from lits"""


class MyList(list):
    """define a class"""
    def print_sorted(self):
        """function to print the list"""
        print(sorted(self))
