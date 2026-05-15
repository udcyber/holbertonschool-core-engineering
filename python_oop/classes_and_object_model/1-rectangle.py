#!/usr/bin/env python3
"""Define a class [Rectangle] with width and height"""


class Rectangle:
    """Definition of [Rectangle]"""
    def __init__(self, width=0, height=0):
        """
        Arguments:
            height: height of the rectangle
            width: width of the rectangle
        Raises:
            TypeError: width or heigth is not integer
            ValueError: width or height is not integer
        """
        # raise exceptions for width and height
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        # width and heigh are private
        self.__width = width
        self.__height = height

    # getter for width
    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    # setter for width
    @width.setter
    def width(self, value):
        """Set a value for the width of the rectangle"""
        # raise exceptions for value of width
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # getter for height
    @property
    def height(self):
        """Return the height of the rectangle"""
        return self.__height

    # setter for height
    @height.setter
    def height(self, value):
        """Set a value for the height of the rectangle"""
        # raise exceptions for value of height
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
