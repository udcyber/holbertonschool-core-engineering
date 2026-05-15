#!/usr/bin/env python3
"""Extend the Square class"""


Rectangle = __import__("2-rectangle").Rectangle


class Square(Rectangle):
    """Definition of Square"""
    def __init__(self, size):
        # call the parent class Rectangle's __init__
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        # str returns [Square] <width>/<height>
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
