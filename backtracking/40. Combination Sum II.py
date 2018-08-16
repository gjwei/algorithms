# coding: utf-8
# Author: gjwei

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates = sorted(candidates)
        self.backtracking(candidates, 0, target, [], result)
        return result

    def backtracking(self, nums, index, target, cur_list, result):
        if target == 0:
            result.append(cur_list[:])
            return
        if index == len(nums) or target < 0:
            return

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            cur_list.append(nums[i])
            self.backtracking(nums, i + 1, target - nums[i], cur_list, result)
            cur_list.pop()
        return