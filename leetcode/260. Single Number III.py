# coding: utf-8


def single_num3(nums):
    xor = 0
    for n in nums:
        xor ^= n

    xor_with_1 = xor & (~(xor - 1))
    r1, r2 = 0, 0

    for n in nums:
        if n & xor_with_1 == 0:
            r1 ^= n
        else:
            r2 ^= n

    return r1, r2
            