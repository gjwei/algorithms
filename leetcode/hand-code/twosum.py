# coding: utf-8

# hash table
def two_sum(nums, target):
    d = {}
    for i, n in enumerate(nums):
        if target - n not in d:
            d[n] = i
        else:
            return (d[target - n], i)
    return (-1, -1)

    