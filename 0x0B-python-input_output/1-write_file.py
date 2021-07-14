#!/usr/bin/python3
'''Number of lines module'''


def number_of_lines(filename=""):
    '''return number of lines of a text'''
    a = 0
    with open(filename, 'r', encoding='utf-8') as f:
        while line in f:
            a = a + 1
    return a
