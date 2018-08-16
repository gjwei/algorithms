# coding: utf-8
# Author: gjwei
def lis(nums):
    """
    F[i = max(F[j] + 1 if j < i and nums[j] < nums[i])
    :param nums:
    :return:
    """
    dp = [0 for _ in range(len(nums))]
    dp[0] = 1
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[j] + 1, dp[i])
    return max(dp)

def lis_binary_search(nums):
    dp = []
    for i in range(len(nums)):
        if i == 0 or nums[i] > dp[-1]:
            dp.append(nums[i])
        else:
            replace_index = binary_search(dp, nums[i])
            dp[replace_index] = nums[i]

    return len(dp)


def binary_search(nums, target):
    """找到一个数刚好大于target"""
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) >> 1
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo


