#!/usr/bin/python3
"""Write a class MyList"""


class MyList(list):
    """  that inherits from list """

    def print_sorted(self):
        print(sorted(self))
