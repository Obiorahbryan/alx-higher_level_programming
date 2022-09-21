#!/usr/bin/python3

for i in range(8):
    for j in range(10):
        if j <= i:
            continue
        print("{n:d}{m:d}".format(n=i, m=j), end=', ')
print(89)
