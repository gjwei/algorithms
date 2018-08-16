# coding: utf-8
# Author: gjwei
"""
含有重复的元素时候的全排列
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        visited = [False for _ in range(len(nums))]
        self.backtracking(nums, visited, [], result)
        return result


    def backtracking(self, nums, visited, tmp, result):
        if len(tmp) == len(nums):
            result.append(tmp[:])
            return

        for i in range(len(nums)):
            if visited[i] or (i > 0 and (not visited[i - 1]) and nums[i] == nums[i - 1]):
                continue

            tmp.append(nums[i])
            visited[i] = True
            self.backtracking(nums, visited, tmp, result)
            visited[i] = False
            tmp.pop()

        return
