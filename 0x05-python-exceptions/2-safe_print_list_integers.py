#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Args:
        my_list: the lst to be printed
        x: the number element of the list
    Return:
        the number of elements
    """
    counter = 0
    for i in range(0, x):
        try:
            print('{:d}'.format(my_list[i]), end="")
            counter += 1
        except (ValueError, TypeError):
            continue
    print()
    return (counter)
