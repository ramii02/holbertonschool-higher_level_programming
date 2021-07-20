#!/usr/bin/python3
"""class Square"""


class Square:
    """class square"""

    def __init__(self, size=0):
        """initialize with attributes"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """sets size with error handling"""
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """to find area of square"""
        return self.__size * self.__size

    def __lt__(self, other):
        """less than"""
        return self.area() < other.area()

    def __le__(self, other):
        """less than or equals"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """equal to"""
        return self.area() == other.area()

    def __ne__(self, other):
        """not equal to"""
        return self.area() != other.area()

    def __gt__(self, other):
        """greater than"""
        return self.area() > other.area()

    def __ge__(self, other):
        """greater than"""
        return self.area() >= other.area()
