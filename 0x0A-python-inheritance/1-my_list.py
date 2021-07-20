#!/usr/bin/python3
"""
1-my_list
"""


class MyList(list):
    """
    prints to stdout list in order
    """

    def print_sorted(self):
        """
        prints the list
        """
        sorted_list = MyList()
        for item in self:
            sorted_list.append(item)
        print(sorted(sorted_list))
