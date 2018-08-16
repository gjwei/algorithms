# coding: utf-8
# Author: gjwei
"""
Given a collection of distinct integers, return all possible permutations.

"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        visited = [False for _ in range(len(nums))]
        self.backtracking(nums, visited, [], result)
        return result

    def backtracking(self, nums, visited, tmp, result):
        if len(tmp) == len(nums):
            result.append(tmp[:])
            return
        for i in range(len(nums)):
            if not visited[i]:
                tmp.append(nums[i])
                visited[i] = True
                self.backtracking(nums, visited, tmp, result)
                visited[i] = False
                tmp.pop()
        return
