# coding: utf-8
# Author: gjwei
"""
冒泡排序法
"""
def bubble_sort(nums):
    has_sorted = False

    for i in range(0, len(nums)):
        if has_sorted:
            break
        has_sorted = True
        for j in range(0, len(nums) - i - 1):
            if nums[j + 1] < nums[j]:
                has_sorted = False
                nums[j], nums[j + 1]  = nums[j + 1], nums[j]
