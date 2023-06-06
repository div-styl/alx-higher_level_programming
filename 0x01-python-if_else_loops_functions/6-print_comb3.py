#!/usr/bin/python3
for i in range(10):
    for d in range(i + 1, 10):
        if i == 8 and d == 9:
            print("{}{}".format(i, d))
            print()
        else:
            print('{}{}'.format(i, d), end=', ')
