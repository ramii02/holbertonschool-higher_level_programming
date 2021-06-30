#!/usr/bin/python3
""" returns the number of characters written """


def number_of_lines(filename=""):
    """  filename to read the number of lines """
    i = 0
    with open(filename, 'r') as f:
        for star in f:
            i += 1
    return i
