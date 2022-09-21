#!/usr/bin/python3

for i in range(97, 97 + 26):
    if i in (101, 113):
        continue
    print("{ch:c}".format(ch=i), end='')
