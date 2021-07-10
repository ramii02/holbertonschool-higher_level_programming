#!/usr/bin/python3
""" subclass of list """

class MyList(list):
    """ display sorted list """

    def print_sorted(self):
        """ sorts list and print """
        n_list = self[:]
        n_list.sort()
        print(n_list)
