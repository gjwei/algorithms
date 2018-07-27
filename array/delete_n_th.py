# coding: utf-8
# Author: gjwei
"""将数组中重复次数多余k的元素删掉"""
from collections import defaultdict


def delete_k_dup(nums, k):
    result = []
    d = defaultdict(int)

    for i, v in enumerate(nums):
        if d[v] < k:
            result.append(v)
        d[v] += 1
    return result