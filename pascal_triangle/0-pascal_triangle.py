#!/usr/bin/python3
"""a function that returns a list of lists of integers
representing the Pascal's triangle of n"""


def pascal_triangle(n):
    """a function that returns a list of lists of integers
    representing the Pascal's triangle of n"""
    if n <= 0:
        return []

    pascal = [[1]]
    for i in range(1, n):
        row = [1]
        prev_row = pascal[i - 1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        pascal.append(row)
    return pascal
