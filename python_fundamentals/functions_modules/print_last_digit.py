#!/usr/bin/env python3

# Print the last digit of number
# Return: the value of the last digit

def print_last_digit(number):
    """print last digit of number, always positive"""
    if number < 0:
        print(number % -10)
    else:
        print(number % 10)