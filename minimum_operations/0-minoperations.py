#!/usr/bin/python3
"""
This script calculates the minimum number of operations needed to achieve
exactly n "H" characters in a file, starting with one "H". The operations allowed
are "Copy All" and "Paste".
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


if __name__ == "__main__":
    n = int(input("Enter the number of H characters you want: "))

    result = minop(n)
    print(f"Min number of operations to reach {n} characters: {result}")
