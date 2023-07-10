#!/usr/bin/python3
"""
Containing the class BaseGeometry
"""


class BaseGeometry:
    """the class with public attribute area"""
    def area(self):
        """raising an exception when called"""
        raise Exception("area() is not implemented")
