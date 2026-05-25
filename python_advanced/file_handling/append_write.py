#!/usr/bin/env python3
"""A function that appends a string at the end of a text file (UTF-8)
and returns the number of characters added."""


def append_write(filename="", text=""):
    """Append a string at the end of a text file, interpret it as unicode and
    return the number of characters added
    
    Args:
        filename (str): Name of the file.
        text (str): String to append at the end of the text file.

    Returns:
        Number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        return my_file.write(text)
