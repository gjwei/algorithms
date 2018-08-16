# coding: utf-8
# Author: gjwei

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign = 1
        index = 0
        result = 0
        # 去除开始的空格
        while index < len(str) and str[index] == ' ':
            index += 1
        if index == len(str):
            return 0
        if str[index] == '-' or str[index] == '+':
            sign = -1 if str[index] == '-' else 1
            index += 1
        MAX = 2 << 30
        while index < len(str) and '0' <= str[index] <= '9':
            result = result * 10 + int(str[index])
            index += 1
            if result > MAX:
                result = MAX - 1 if sign == 1 else -MAX
                break

        return sign * result