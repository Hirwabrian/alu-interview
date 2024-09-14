#!/usr/bin/python3
"""method that calculates the minimum number of operations"""


def minop(n):
    """method that calculates the minimum number of operations"""

    div = 2
    operations = 0
    if n <= 0:
        return 0
    else:
        while n > 1:
            while n % div == 0:
                operations = operations + div
                n = n // div
            div = div + 1
        return operations


if __name__ == "__main__":
    n = int(input("Enter the number of H characters you want: "))

    result = minop(n)
    print(f"Min number of operations to reach {n} characters: {result}")
