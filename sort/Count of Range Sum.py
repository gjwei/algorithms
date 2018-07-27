# coding: utf-8
# Author: gjwei
"""
https://leetcode.com/problems/count-of-range-sum/description/
"""
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sums = [0]
        for i in range(nums):
            sums.append(nums[i] + sums[-1])

        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                if upper >= sums[j] - sums[i] >= lower:
                    result += 1
        return result
