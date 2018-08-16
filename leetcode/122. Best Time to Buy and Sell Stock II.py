# coding: utf-8
# Author: gjwei

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0

        for i in range(1, prices):
            result += max(0, prices[i] - prices[i - 1])

        return result