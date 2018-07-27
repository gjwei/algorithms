# coding: utf-8
# Author: gjwei

def swap_nums(a, b):
    a = a - b
    b = a + b
    a = b - a
    return  a, b

def swap_nums_2(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b