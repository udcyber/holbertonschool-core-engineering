#!/usr/bin/env python3

# Print the string in uppercase
# followed by a new line
# Return: nothing

# Function
def uppercase(str):
    """Print string in uppercase"""
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            x = chr(ord(x) - 32)
        print("{}".format(x), end="")
    print("")
