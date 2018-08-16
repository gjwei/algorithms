# coding: utf-8
# Author: gjwei

def max_sum_non_adjacent(nums):
    """choice or not choice
    F[i] = max(F[i - 1], F[i - 2] + nums[i])
    """
    p1, p2 = 0, 0
    for i in range(len(nums)):
        r = max(p1, p2 + nums[i])
        p1, p2 = r, p1
    return r

