#!/usr/bin/python3
"""class Square"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """initialize with size attribute"""
        self.size = size

    @property
    def size(self):
        """gets size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size w/error handling"""
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """finds area of square"""
        return self.__size * self.__size

    def my_print(self):
        """prints square"""
        if self.size == 0:
            print("")
        else:
            for y in range(self.__size):
                for x in range(self.__size):
                    print("#", end="")
                print("")*
