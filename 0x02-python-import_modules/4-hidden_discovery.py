#!/usr/bin/python3
if __name__ == '__main__':
    """
    this program uncover the hidden code of a compiled
    program it listing the name of functions using the
    built-in func dir() except the ones
    that start (__)
    """
import hidden_4
list_names = dir(hidden_4)
for new_list in list_names:
    if new_list[:2] != '__':
        print('{}'.format(new_list))
