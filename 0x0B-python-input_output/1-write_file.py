#!/usr/bin/python3
""" read from a file per lines """


def number_of_lines(filename=""):
    """ reads each line of a file """
    n_lines = 0
    with open(filename, encoding='utf-8') as a_file:
        for a_line in a_file:
            n_lines += 1

    return n_lines
#!/usr/bin/python3
""" Write a function that returns the number of characters written """


def number_of_lines(filename=""):
    """ line of the number """
    i = 0
    with open(filename, 'r') as f:
        for star in f:
            i += 1
    return i
