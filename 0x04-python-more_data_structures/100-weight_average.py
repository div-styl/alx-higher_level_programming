#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    num = sum(y[0] * y[1] for y in my_list)
    num2 = sum(y[1] for y in my_list)
    return num / num2
