#!/usr/bin/python3

import random

numbers = random.randint(-10000, 10000)
digit = abs(numbers) % 10
if numbers < 0:
    digit = -digit
print(f"Last digit of {numbers:d} is {digit:d} and is ", end="")
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
