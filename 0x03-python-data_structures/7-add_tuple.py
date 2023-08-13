#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # using tuple unpacking
    a1, a2 = tuple_a[:2]
    b1, b2 = tuple_b[:2]

    sum_tuple = (a1 + b2, a2 + b2)

    return sum_tuple
