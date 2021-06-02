#!/usr/bin/python3
""" Write a function that writes a string to a text file """


def number_of_lines(filename=""):
    """ returns the number of characters written """
    with open(filename, 'r') as f:
        count = 0
        for line in f:
            count += 1
    return count
