#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """delete an element  in the list at specific index"""
    len_lst = len(my_list)
    if idx < 0 or idx >= len_lst:
        return (my_list)
    my_list.remove(my_list[idx])
    return my_list
