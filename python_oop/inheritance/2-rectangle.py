#!/usr/bin/env python3
"""Extend the [Rectangle class]"""
# add area()


BaseGeometry = __import__("base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """"Definition of [Rectangle]"""
    def __init__(self, width, height):
        # validation for exceptions for width and height of [Rectangle]
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    # str() returns [Rectangle] <width>/<height>
    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
