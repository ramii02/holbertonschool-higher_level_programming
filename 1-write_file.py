#!/usr/bin/python3
"""  returns the number of characters written """


def number_of_lines(filename=""):
    with open(filename, 'r') as f:
        count = 0
        for line in f:
            count += 1
    return count
