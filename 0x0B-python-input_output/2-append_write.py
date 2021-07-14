#!/usr/bin/python3
'''reads n lines of text file'''


def read_lines(filename="", nb_lines=0):
    '''read lines funct'''
    i = 0
    with open(filename, 'r', encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            while line in f:
                if i < nb_lines:
                    print(line, end="")
                i = i + 1
