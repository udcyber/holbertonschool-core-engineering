#!/usr/bin/env python3
"""A function that writes a string to a text file (UTF-8) and returns
the number of characters written."""


def write_file(filename="", text=""):
    """Write a string to a text file, interpret it as unicode and return
    the number of characters written.

    Args:
        filename (str): Name of the file.
        text (str): String to write to the text file.

    Returns:
        Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)
