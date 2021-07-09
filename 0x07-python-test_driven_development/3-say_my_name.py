#!/usr/bin/python3
""" I have to display My name is <first name> <last name> """


def say_my_name(first_name, last_name=""):
    """ I have to display My name is <first name> <last name> """

    fn = 0
    ln = 0
    if type(first_name) is str:
        fn = 1
    elif not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if type(last_name) is str:
        ln = 1
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if fn == 1 and ln == 0:
        print("My name is {} ".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
