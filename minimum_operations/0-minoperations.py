#!/usr/bin/python3
"""
Function that calculates the min operations to copy and paste letters
"""


def minop(n):
    """
    Method that calculates the minimum number of operations required to get
    exactly `n` "H" characters.

    Args:
    n (int): The target number of "H" characters.

    Returns:The minimum number of operations required to get `n` "H" characters.
    """
    div = 2  
    operations = 0  

    if n <= 0:
        return 0
    else:
        while n > 1:
            while n % div == 0:
                operations += div
                n //= div
            div += 1
        return operations
