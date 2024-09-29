#!usr/bin/python3

def rain(walls):
    """Function to return the maximum water that can be stored"""
    water = 0
    for i in range(1, len(walls)-1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])

        right = walls[i]
        for j in range(i+1, len(walls)):
            right = max(right, walls[j])

        water += min(left, right) - walls[i]
    
    return water