#!/usr/bin/python3
"""define a func pascal_triangle.py"""


def pascal_triangle(n):
    """
    returns a list of lists of
    integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return []
    trian = [[1]]
    while len(trian) != n:
        tri = trian[-1]
        tmpo = [1]
        for i in range(len(tri) - 1):
            tmpo.append(tri[i] + tri[i + 1])
        tmpo.append(1)
        trian.append(tmpo)
    return trian
