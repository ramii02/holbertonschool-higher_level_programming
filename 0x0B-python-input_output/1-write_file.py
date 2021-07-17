#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, mode='r', encoding='utf-8') as texter:
        text = texter.read()
        cont = text.count("\n")
        return cont
