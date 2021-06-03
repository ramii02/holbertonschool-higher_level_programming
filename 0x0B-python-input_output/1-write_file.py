#!/usr/bin/python3
""" writes a string to a text file """


def number_of_lines(filename=""):
    """ returns the number of characters written """
    n_lines = 0
    with open(filename, encoding='utf-8') as a_file:
        for a_line in a_file:
            n_lines += 1

    return n_lines
