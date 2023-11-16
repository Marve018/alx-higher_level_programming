#!/usr/bin/python3
"""
    A moudle that performes the addition operation between
    two integers or floats.
"""

def add_integer(a, b=98):
    """ Add two numbers
        arguments a & b must be integers or floats,
        otherwise raise a TypeError.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
