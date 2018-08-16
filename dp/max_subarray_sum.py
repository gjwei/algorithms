# coding: utf-8
# Author: gjwei
def max_sub_sum(nums):
    result = 0
    dp = [0]
    for i in range(len(nums)):
        dp.append(max(nums[i] + dp[-1]), 0)
    return max(dp)