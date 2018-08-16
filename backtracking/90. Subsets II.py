# coding: utf-8
# Author: gjwei
"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums = sorted(nums)


    def backtracking(self, nums, index, tmp, result):
        if index > len(nums):
            return
        result.append(tmp[:])

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue

            tmp.append(nums[i])
            self.backtracking(nums, i + 1, tmp, result)
            tmp.pop()

        return