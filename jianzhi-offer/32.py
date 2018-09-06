# coding: utf-8

# 从1到n整数中，1出现的次数


def count1s(n):
    if n == 0:
        return 0
    if n < 10:
        return 1

    n = str(n)
    head = int(n[0])
    tail = int(n[1:])
    if head == 1:
        return count1s(10 ** (len(n) - 1) - 1) + tail + 1 + count1s(tail)
    else:
        return head * count1s(10 ** (len(n) - 1) - 1) + 10 ** (len(n) - 1) + count1s(n % (10 ** (len(n) - 1)))