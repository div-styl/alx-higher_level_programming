#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for _ in range(1):
    if number < 0:
        print(f'{number} is negative')
    elif number > 0:
        print(f'{number} is positive')
    elif number == 0:
        print(f'{number} is zero')
