#!/usr/bin/env python
#-*- coding:utf-8 -*- 
#Author: gjwei

def count_1s(n):
    result = 0

    while n:
        result += 1
        n &= (n - 1)
    return result

def hello(a):
    print(a)

if __name__ == '__main__':
    n = 3
    print(count_1s(n))

