#!/usr/bin/python3

# Author -Bamidele Adefolaju

r = 0
for k in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(k - r)), end="")
    r = 32 if r == 0 else 0
