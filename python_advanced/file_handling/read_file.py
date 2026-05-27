#!/usr/bin/env python3
"""A function that reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """Read a file, interpret it as unicode and print it to stdout.

    Args:
        filename (str): Name of the file.

    Return:
        nothing
    """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read(), end="")
