#!/usr/bin/python3
"""square class"""


class Square:
    """initialize square with size"""

    def __init__(self, size=0):
        """initialize square with variables"""
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """to find area of square"""
        return self.__size * self.__size
