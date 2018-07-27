# coding: utf-8
# Author: gjwei
def find_kth_smallest(nums, k):
    assert 0 < k <= len(nums)
    low, high = 0, len(nums) - 1
    while low <= high:
        p_index = partition(nums, low, high)
        if p_index + 1 < k:
            low = p_index + 1
        elif p_index + 1 == k:
            return nums[k - 1]
        else:
            high = p_index - 1
    return -1



def partition(nums, low, high):
    if low >= high:
        return -1
    pivot = nums[high]
    index = low
    for i in range(low, high + 1):
        if nums[i] <= pivot:
            nums[index], nums[i] = nums[i], nums[index]
            index += 1
    return index - 1

import random

def random_shuffle(nums):
    for i in range(len(nums)):
        r = random.randint(0, i)
        nums[i], nums[r] = nums[r], nums[i]
    return
