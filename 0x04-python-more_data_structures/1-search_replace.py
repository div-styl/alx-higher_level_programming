#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for idx, New_value in enumerate(new_list):
        if New_value != search:
            return (my_list)
        if New_value == search:
            new_list[idx] = replace
    return (new_list)
