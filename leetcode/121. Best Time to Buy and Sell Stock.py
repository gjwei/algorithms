# coding: utf-8
# Author: gjwei

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        min_prices = prices[0]

        for i in range(1, len(prices)):
            min_prices = min(prices[i], min_prices)
            result = max(result, prices[i] - min_prices)
        return result