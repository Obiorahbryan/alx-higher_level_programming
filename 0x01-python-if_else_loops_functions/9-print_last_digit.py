#!/usr/bin/python3

def print_last_digit(n):
    """prints the last digit of a number"""
    ld = abs(n) % 10
    print(ld, end='')
    return ld
