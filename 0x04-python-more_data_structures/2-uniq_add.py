#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    uniq_num = set(my_list)
    for num in uniq_num:
        total += num
    return total
