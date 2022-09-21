#!/usr/bin/python3

for i in range(97 + 25, 96, -1):
    if i % 2:
        i -= 32
    print("{ch:c}".format(ch=i), end='')
