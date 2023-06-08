#!/usr/bin/python3
if __name__ =="__main__":
    """small calculatore that calculator assigned
    values
    """
from calculator_1 import *
numo = 10
nums = 5
print('{} + {} = {}'.format(numo, nums, add(numo, nums)))
print('{} + {} = {}'.format(numo, nums, sub(numo, nums)))
print('{} + {} = {}'.format(numo, nums, mul(numo, nums)))
print('{} + {} = {}'.format(numo, nums, div(numo, nums)))
