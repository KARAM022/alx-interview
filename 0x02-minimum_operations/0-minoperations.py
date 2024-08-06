#!/usr/bin/python3
"""
minOperations
"""

def minOperations(n):
    """
    Calculate the fewest number of operations needed to reach a target number of H characters.
    
    Args:
        n (int): H characters.
    
    Returns:
        int: The fewest number of operations needed, or 0 if impossible.
    """
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations
