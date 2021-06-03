#!/usr/bin/python3
""" Write a function that returns the number of characters written """


def number_of_lines(filename=""):
    """ the number of lines """
    i = 0
    with open(filename, 'r') as f:
        for star in f:
            i += 1
    return i
