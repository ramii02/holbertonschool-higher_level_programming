#!/usr/bin/python3
""" return the sum of a + b """


def add_integer(a, b=98):
    """ return the sum of a + b """

    if type(a) is float or type(a) is int:
        a = int(a)
    else:
        raise TypeError('a must be an integer')
    if type(b) is float or type(b) is int:
        b = int(b)
    else:
        raise TypeError('b must be an integer')
    return a + b
