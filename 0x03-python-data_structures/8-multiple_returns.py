#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_n = (len(sentence), sentence[0])
    if len(sentence) == 0:
        return None
    return tuple_n
