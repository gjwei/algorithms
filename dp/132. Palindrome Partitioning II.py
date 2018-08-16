# coding: utf-8
# Author: gjwei
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0]
        for i in range(1, len(s)):
            r = dp[i - 1] + 1
            for j in range(i):
                if self.is_p(s, j, i):
                    if j == 0:
                        r = 0
                    else:
                        r = min(r, dp[j - 1] + 1)
            dp.append(r)
        return dp[-1]


    def is_p(self, s, left, right):
        if left > right:
            return False
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
