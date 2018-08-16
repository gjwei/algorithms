# coding: utf-8
# Author: gjwei

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        sells = [0]
        buys = [-prices[0]]

        for i in range(1, len(prices)):
            sells[i] = max(sells[i - 1], buys[i - 1] + prices[i])
            buys[i] = max(buys[i - 1], sells[i - 2] - prices[i])

        return sells[-1]