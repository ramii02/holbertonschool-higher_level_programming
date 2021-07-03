#!/usr/bin/python3
"""
defines the number_of_lines function
"""


def number_of_lines(filename=""):
    """
    returns the number of lines of a text file
    """
    with open(filename, encoding="utf-8") as file:
        nlines = 0
        while line in file:
            nlines += 1
    return nlines
