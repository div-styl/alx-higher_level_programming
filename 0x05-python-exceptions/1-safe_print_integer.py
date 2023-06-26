#!/usr/bin/python3
def safe_print_integer(value):
    """
    argu:
        value: the interger to be printed
    Return:
        priny the integer if it isn't print error
    """
    try:
        print('{:d}'.format(value))
        return (True)
    except (ValueError, TypeError):
        return (False)
