#!/usr/bin/python3
""" Define a class square """


class Square:
    """ this is a class """
    def __init__(self, size=0):
        """ Initialize
        Args:
            size (int): size of square.
        """
        self.__size = size

        @property
        def size(self):
            """Get/set the current size of the square."""
            return self.__size

        @size.setter
        def size(self, value):
            if type(value) != int:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

                def area(self):
                    """Return the current area of the square."""
                    return self.__size * self.__size
