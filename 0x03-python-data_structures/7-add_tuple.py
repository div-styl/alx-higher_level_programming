#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    rslt_0 = 0
    rslt_1 = 0
    if len(tuple_a) > 0:
        rslt_0 += tuple_a[0]
    if len(tuple_a) > 1:
        rslt_1 += tuple_a[1]
    if len(tuple_b) > 0:
        rslt_0 += tuple_b[0]
    if len(tuple_b) > 1:
        rslt_1 += tuple_b[1]
    return (rslt_0, rslt_1)
