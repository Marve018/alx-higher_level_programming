#!/usr/bin/python3
"""
    Text_indentation moudle
    Moudle contains a function that performs text indentation
"""

def text_indentation(text):
    """
        function that prints a text with 2 new lines.
        after each of these characters: ., ? and :
    """
    m = 0
    if type(text) != str:
        raise TypeError("text must be a string")
    text1 = text.replace('?', '?\n\n')
    text1 = text1.replace('.', '?\n\n')
    text1 = text1.replace(':', '?\n\n')
    print("\n".join([i.strip() for i in text1.split("\n")]), end="")
