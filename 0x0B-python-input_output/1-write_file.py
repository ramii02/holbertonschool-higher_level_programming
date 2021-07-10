#!/usr/bin/python3
""" returns number of lines in text file
"""


def number_of_lines(filename=""):
    """
    number of lines
    """

    line_numbers = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            line_numbers += 1

    return line_numbers
