#!/usr/bin/env python3
for i in range(100):
    if i != 99:
        print(i // 10, i % 10, sep="", end=", ")
    else:
        print(i // 10, i % 10, sep="")
