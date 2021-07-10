#!/usr/bin/python3
"""square class"""


class Square:
    """Defines a square by size.
    Attributes:
        size (int): square size"""

    def __init__(self, size=0):
        """initialize square with variables"""
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Calculates the square area.
        Returns:
        int: the current square area."""
        return self.__size * self.__size
