#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """returns a list of lists
    of integers representing the Pascal’s triangle of n
    """

    result = []
    if m > 0:
        for i in range(1, m + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            result.append(level)
    return result
