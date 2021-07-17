#!/usr/bin/python3
"""class square"""


class Square:
    """square class"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize with attributes"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """gets position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets position w/error handling"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in range(len(value)):
            if value[i] < 0:
                raise ValueError("size must be >= 0")
            if len(value) != 2:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    def area(self):
        """finds area of square"""
        return self.__size * self.__size

    def my_print(self):
        """prints square"""
        if self.__size > 0:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for blanks in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
