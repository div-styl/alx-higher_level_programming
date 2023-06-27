#!/usr/bin/python3
def magic_calculation(a, b):
    rslt = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                rslt += a ** b / i
        except (TypeError, IndexError, ValueError):
            rslt = b + a
            break
    return rslt
