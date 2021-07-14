#!/usr/bin/python3
'''Number of lines module'''


def number_of_lines(filename=""):
    '''return number of lines of a text'''
    numlines = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            numlines = numlines + 1
    return numlines
