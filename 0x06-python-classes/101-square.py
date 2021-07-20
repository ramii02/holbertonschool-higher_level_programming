#!/usr/bin/python3
"""class square"""


class Square:
    """square class"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize with attributes"""
        self.size = size
        self.position = position

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
        s = "position must be a tuple of 2 positive integers"
        if type(value) is tuple:
            if len(value) != 2:
                raise TypeError(s)
            else:
                for i in range(len(value)):
                    if value[i] < 0:
                        raise TypeError(s)
            self.__position = value
        else:
            raise TypeError(s)

    def area(self):
        """finds area of square"""
        return self.__size * self.__size

    def my_print(self):
        """prints square"""
        if self.size == 0:
            print("")
        else:
            for num in range(self.__position[1]):
                print("")
            for y in range(self.__size):
                for x in range(self.__size + self.__position[0]):
                    if x < self.__position[0]:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print("")

    def __str__(self):
        """print squre instance"""
        if self.size == 0:
            return ("")
        else:
            string = ""
            for num in range(self.__position[1]):
                string += "\n"
            for y in range(self.__size):
                for x in range(self.__size + self.__position[0]):
                    if x < self.__position[0]:
                        string += " "
                    else:
                        string += "#"
                string += "\n"
            string = string[:-1]
            return string
