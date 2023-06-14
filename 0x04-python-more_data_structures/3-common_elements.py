#!/usr/bin/python3
def common_elements(set_1, set_2):
    comman_ele = set()
    for elem in set_1:
        if elem in set_2:
            comman_ele.add(elem)
    return comman_ele
