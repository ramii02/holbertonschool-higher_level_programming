#!/usr/bin/python3
'''class print_square'''


def print_square(size):
    ''' function that prints square of size size with '#' '''

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    while i in range(size):
        print('#' * size)
