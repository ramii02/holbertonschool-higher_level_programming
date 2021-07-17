#!/usr/bin/python3
"""
>>> print_square(4)
####
####
####
####
"""


def print_square(size):
    """
    >>> c = print_square(4)
    """
    if type(size) is float:
        if size < 0:
            raise TypeError('size must be an integer')
        size = int(size)
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#' * size)
