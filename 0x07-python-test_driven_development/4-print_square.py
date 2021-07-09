#!/usr/bin/python3
""" I have to display with '#' """


def print_square(size):
""" i have to display with '#' """

    if isinstance(size, int):
        for i in range(size):
            for j in range(size):
                print('#', end="")
            print()
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
s