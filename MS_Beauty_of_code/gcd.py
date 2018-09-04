#!/usr/bin/env python
#-*- coding:utf-8 -*- 
#Author: gjwei

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


