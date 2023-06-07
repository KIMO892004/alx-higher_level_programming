#!/usr/bin/python3

# Author - Bamidele Adefolaju

def magic_calculation(k, r, q):
    """Matching bytecode provided by Holberton School."""
    if k < r:
        return (q)
    if q > r:
        return (k + r)
    return (k*r - q)
