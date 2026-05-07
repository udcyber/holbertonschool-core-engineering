#!/usr/bin/env python3

# Print the last digit of number
# Return: the value of the last digit

def print_last_digit(number):
    """print last digit of number, always positive"""
    print(abs(number) % 10, end="")

    return (abs(number) % 10)
