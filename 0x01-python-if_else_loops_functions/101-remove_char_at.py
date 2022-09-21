#!/usr/bin/python3

def remove_char_at(s, i):
    """removes a character at index i"""
    if i < 0:
        return s
    return s[:i] + s[i+1:]


if __name__ == '__main__':
    print(remove_char_at("Best School", 3))
    print(remove_char_at("Chicago", 2))
