# coding: utf-8
# nums已经有序了

def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s > target:
            right -= 1
        elif s < target:
            left += 1
        else:
            return (left, right)
    return (-1, -1)