#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
remainder = number % 10
flag = True
lt = 'and is less than 6 and not 0'
while flag:
    if remainder > 5:
        print(f'Last digit of {number} is {remainder} and is greater than 5')
    elif remainder == 0:
        print(f'Last digit of {number} is {remainder} is 0 and is 0')
    elif remainder < 6:
        print(f'Last digit of {number} is {remainder} {lt}')
    flag = False
