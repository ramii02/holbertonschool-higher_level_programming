#!/usr/bin/python3
""" the procedure of this module is the beginning of classes """


class Square():
    """ Write a class Square that defines a square """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
