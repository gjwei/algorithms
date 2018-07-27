# coding: utf-8
# Author: gjwei
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for _ in range(len(p) + 1)]  for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(len(s)):
            for j in range(len(p)):

