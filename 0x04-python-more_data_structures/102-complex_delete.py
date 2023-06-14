#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())
    for idx in keys:
        if value == a_dictionary.get(idx):
            del a_dictionary[idx]
    return a_dictionary
