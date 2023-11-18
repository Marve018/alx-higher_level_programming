#!/usr/bin/python3
"""
    This module demonstrates documentation as specified by the `Google Python
    Module contains a function that prints out a name
"""


def say_my_name(first_name, last_name=""):
    """Example of add on the say_my_name method.
            this functions print the name
        """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
