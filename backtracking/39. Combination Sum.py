# coding: utf-8
# Author: gjwei
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtracking(candidates, 0, target, [], 0, result)
        return result

    def backtracking(self, nums, index, target, cur_list, cur_sum, result):
        if cur_sum == target:
            result.append(cur_list[:])
            return
        if cur_sum > target or index >= len(nums):
            return

        for i in range(index, len(nums)):
            cur_sum += nums[i]
            cur_list.append(nums[i])
            self.backtracking(nums, i, target, cur_list, cur_sum, result)
            cur_list.pop()
            cur_sum -= nums[i]
        return