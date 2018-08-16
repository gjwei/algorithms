# coding: utf-8
# Author: gjwei

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.backtracking(s, 0, [], result)
        return result

    def backtracking(self, s, index, tmp, result):
        if index >= len(s):
            result.append(tmp[:])
            return

        for i in range(index, len(s)):
            if self.is_palin(s[index: i + 1]):
                tmp.append(s[index: i + 1])
                self.backtracking(s, i + 1, tmp, result)
                tmp.pop()
        return

    def is_palin(self, s):
        if len(s) == 0:
            return False
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True