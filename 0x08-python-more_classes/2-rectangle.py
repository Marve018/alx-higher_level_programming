#!/usr/bin/python3
"""
    Module thaat contains a class Rectangle
    that defines a rectangle
"""


class Rectangle:
    """
       class Rectangle that defines a rectangle
       (based on 1-rectangle.py)
    """

    def __init__(self, width=0, height=0):
        """
            initializer method
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            getter for the width instance
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter for the width instance
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
            getter for the heigth instance
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
           setter for the heigth instance
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
    
    def area(self):
        """
            returns the rectangle area
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
            returns the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width*2) + (self.__height*2))
