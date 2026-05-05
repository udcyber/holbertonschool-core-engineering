#!/usr/bin/env python3
# Given line
number = __import__('random').randint(-10000, 10000)

# Declaration
last_digit = abs(number) % 10

# Output info
print(f"Last digit of {number} is {last_digit} and is", end=" ")

if last_digit < 6 and last_digit != 0:
    print("less than 6 and not 0")

elif last_digit > 5:
    print("greater than 5")

elif last_digit == 0:
    print("0")
