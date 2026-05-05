#!/usr/bin/env python3
# Output info
for x in range(0, 8):
    for y in range(x, 10):
        if x != y:
            print("{:d}{:d}, ".format(x, y), end="")

# Print without comma
print("89")
