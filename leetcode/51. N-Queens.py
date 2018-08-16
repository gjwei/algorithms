# coding: utf-8
# Author: gjwei

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

    def solve(self, row, cols, result, n):
        if row == n:
            result.append(self.translate(cols))
        else:
            for col in range(n):  # 第row行的皇后放在col列的位置
                if self.check_valid(cols, row, col):
                    cols[row] = col
                    self.solve(row + 1, cols, result, n)

    def check_valid(self, cols, row, col):
        for row2 in range(row):
            col2 = cols[row2]

            if col2 == col:
                return False
            if abs(cols[row] - cols[row2]) == row - row2:
                return False
        return True

    def translate(self, cols):
        tmp = [['.'] * len(cols) for _ in range(len(cols))]
        for i in range(len(cols)):
            tmp[i][cols[i]] = 'Q'
        result = []
        for i in range(len(tmp)):
            result.append(''.join(tmp[i]))
        return result

#

