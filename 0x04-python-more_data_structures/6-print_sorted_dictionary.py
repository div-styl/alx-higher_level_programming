#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortd_list = list(a_dictionary.keys())
    sortd_list.sort()
    for key in sortd_list:
        print('{} : {}'.format(key, a_dictionary.get(key)))
