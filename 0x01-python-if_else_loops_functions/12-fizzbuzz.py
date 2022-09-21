#!/usr/bin/python3

def _getFiz(n):
    """Returns the Fizz Buzz value of a number"""
    if not n % 3 and not n % 5:
        return 'FizzBuzz'
    elif not n % 3:
        return 'Fizz'
    elif not n % 5:
        return 'Buzz'
    else:
        return n


def fizzbuzz():
    """prints a fizz buzz from 1 to 100"""
    for i in range(1, 101):
        print(_getFiz(i), end=' ')


if __name__ == '__main__':
    fizzbuzz()
