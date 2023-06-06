#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)
digits = abs(number) % 10
if number < 0:
    digits = -digits
print(f"Last digits of {number:d} is {digits:d} and is ", end="")
if digits > 5:
    print("greater than 5")
elif digits == 0:
    print("0")
else:
    print("less than 6 and not 0")
