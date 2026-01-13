#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description:
        Computes the factorial of an integer using recursion.

    Parameters:
        n (int): The integer for which the factorial is calculated.
                 Must be greater than or equal to 0.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the command-line argument,
# compute its factorial and print the result
f = factorial(int(sys.argv[1]))
print(f)