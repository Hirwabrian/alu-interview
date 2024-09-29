#!/usr/bin/python3
"""
Module to calculate the amount of rainwater that can be trapped
between walls of varying heights after a rainfall.
"""

def rain(walls):
    """
    Calculate the total amount of rainwater that can be trapped
    between the walls represented by a list of non-negative integers.
    
    Args:
        walls (list): A list of non-negative integers representing the 
        heights of walls, where each element has a width of 1 unit.

    Returns:
        int: The total amount of trapped rainwater (in square units).
        If no water can be trapped, or the input list is empty, returns 0.
    
    Example:
        walls = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        The function will return 6 as the total trapped water.
    """
    # Initialize total water trapped to 0
    water = 0

    # If the walls list is empty, immediately return 0
    if len(walls) == 0:
        return water

    # Iterate through each wall, starting from index 1 to len(walls) - 2
    # (since the walls at the very ends can't trap water)
    for i in range(1, len(walls) - 1):
        # Find the maximum height to the left of the current wall
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])

        # Find the maximum height to the right of the current wall
        right = walls[i]
        for j in range(i + 1, len(walls)):
            right = max(right, walls[j])

        # Calculate the trapped water at this wall position
        # It is the minimum of the maximum heights on the left and right
        # minus the current wall height
        water += min(left, right) - walls[i]

    # Return the total trapped water
    return water
