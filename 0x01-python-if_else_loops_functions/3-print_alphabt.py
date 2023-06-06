#!/usr/bin/python3

for letters in range(ord('a'), ord('z') + 1):
    if chr(letters) != 'e' and chr(letters) != 'q':
        print('{:c}'.format(letters), end='')
