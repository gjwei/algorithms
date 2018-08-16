# coding: utf-8
# Author: gjwei

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.backtracking(nums, 0, [], result)
        return result

    def backtracking(self, nums, index, tmp, result):
        if index == len(nums):
            return
        result.append(tmp[:])
        for i in range(index, len(nums)):
            tmp.append(nums[i])
            self.backtracking(nums, i + 1, tmp, result)
            tmp.pop()
        return