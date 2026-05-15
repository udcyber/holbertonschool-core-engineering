#!/usr/bin/env python3
"""Create a class [Rectangle] that inherits from [BaseGeometry]"""
# [Rectangle]
# represents a rectangle
# is defined by its width and height


BaseGeometry = __import__("base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        # validation for exceptions for width and height of [Rectangle]
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
