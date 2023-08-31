#!/usr/bin/python3
""" define a class square """


class Square:
    """this is a class"""
    def __init__(self, size=0):
        """ Initialize
        Args:
            size (int): size of the square.
        """
        try:
            self.__size = size
            if type(size) != int:
                raise TypeError
            elif size < 0:
                raise ValueError
            except TypeError:
                print("size must be an integer", end="")
                raise TypeError
            except ValueError:
                print("size must be >= 0", end="")
                raise ValueError

            def area(self):
                """ area of the square
                Returns:
                    Args (int): size square.
                """
                return self.__size ** 2
