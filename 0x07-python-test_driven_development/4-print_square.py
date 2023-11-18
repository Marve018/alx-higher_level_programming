#!/usr/bin/python3
"""
    This module demonstrates documentation as specified by the `Google Python
    Module contains a function that prints a square
"""


def print_square(size):
    """
        Example of add on the print_square method.
        this functions print a square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
