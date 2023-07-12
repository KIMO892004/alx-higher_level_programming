#!/usr/bin/python3
"""
containing the json str function
"""

import json


def from_json_string(my_str):
    """returning an object represented by a JSON string"""
    return json.loads(my_str)
