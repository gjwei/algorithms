# coding: utf-8
# Author: gjwei
"""
选择排序：每次选择出数据中最小的元素，和第一个元素进行交换。然后从剩下的元素中选择最小的，和第二个元素交换位置
依次进行下去
"""

def select_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

