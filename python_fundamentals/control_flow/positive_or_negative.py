#!/usr/bin/env python3
# Given line
number = __import__('random').randint(-10, 10)

# Functions
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
elif number < 3:
    print(f"{number} is negative")
