#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
r = number % 10
flag = True
while flag:
    if r > 5:
        print(f'Last digit of {number} is {r} and is greater than 5')
    elif r == 0:
        print(f'Last digit of {number} is {r} and is 0')
    elif r < 6:
        print(f'Last digit of {number} is {r} and is less than 6 and not 0')
    flag = False
