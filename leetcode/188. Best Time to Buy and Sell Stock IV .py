# coding: utf-8
# Author: gjwei
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        sells = [0 for _ in range(k)]
        buys = [-(1 << 31) for _ in range(k)]

        for i in range(len(prices)):
            for j in range(k):
                if j == 0:
                    buys[j] = max(buys[j],  - prices[i])
                    sells[j] = max(sells[j], buys[j] + prices[i])
                else:
                    buys[j] = max(buys[j], sells[j - 1] - prices[i])
                    sells[j] = max(sells[j], buys[j] + prices[i])

        return sells[-1]
