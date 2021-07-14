#!/usr/bin/python3
"Function to print squares"


def print_square(size):
    """Arguments
    size: size of the int
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and type(size) is float:
        raise TypeError("size must be an integer")
    for a in range(size):
        print("#" * size)
