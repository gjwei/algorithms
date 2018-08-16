# coding: utf-8
# Author: gjwei

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        sells = [0]
        buys = [-prices[0]]

        for i in range(1, len(prices)):
            sells.append(max(sells[i - 1], buys[i - 1] + prices[i] - 2))
            buys.append(max(buys[i - 1], sells[i - 1] - prices[i]))

        return sells[-1]