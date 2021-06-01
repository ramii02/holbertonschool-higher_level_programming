#!/usr/bin/python3
"""MyList inherits from list."""


class MyList(list):
    """ Print the list"""

    def print_sorted(self):
        print(sorted(self))
