# coding: utf-8
# Author: gjwei
"""
插入排序：排序从左到右进行，每次都有当前元素插入到已经排序的数组中。
"""

def insert_sort(nums):
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
