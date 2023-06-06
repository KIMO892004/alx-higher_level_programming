#!/usr/bin/python3

# Author - bamidele Adefolaju

def remove_char_at(strr, num):
    if num < 0:
        return (strr)
    return (strr[:num] + strr[num+1:])
