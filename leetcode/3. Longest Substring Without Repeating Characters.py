# coding: utf-8
# Author: gjwei
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        result = 0
        start = 0
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
            else:
                start = max(start, d[s[i]] + 1)
                d[s[i]] = i
            result = max(result, i - start + 1)
        return result
