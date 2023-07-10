#!/usr/bin/python3
"""
Containing the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """returning True if obj is an instance or inherited from a_class, else False"""
    return (isinstance(obj, a_class))
