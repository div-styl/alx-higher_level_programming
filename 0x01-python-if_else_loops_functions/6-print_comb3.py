#!/usr/bin/python3
for i in range(10):
    for d in range(i + 1, 10):
        if i == 8 and i == 9:
            print("{}{}".format(i, d))
        else:
            print('{}{}'.format(i, d), end=', ')
print()
