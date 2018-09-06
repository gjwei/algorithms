# coding: utf-8


def atoi(s):
    r = 0
    index = 0
    while s[index] == ' ':
        index += 1

    if index == len(s):
        return r
    
    sign = 1

    if s[index] == '+' or s[index] == '-':
        if s[index] == '-':
            sign = -1
        index += 1

    while index < len(s):
        if '0' <= s[index] <= '9':
            r = r * 10 + int(s[index])
            index += 1
        else:
            return 0

    return sign * r