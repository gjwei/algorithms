#!/usr/bin/env python
#-*- coding:utf-8 -*- 
#Author: gjwei
import sys

def solution(matrix, dp, reverse_dp, row,  col, H, W):

    r1 = dp[row - 1][col - 1]
    r2 = reverse_dp[H - row][W - col]
    if r2 == 0:
        return 0
    return (r1 * r2) % (10 ** 9 + 7)


def get_dp(matrix, H, W):
    dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    # 0, 0 > row, col
    dp[0][0] = 1

    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if i == 0 and dp[i][j - 1] > 0 and matrix[i][j] == '.':
                dp[i][j] = dp[i][j - 1]
            if j == 0 and dp[i - 1][j] > 0 and matrix[i][j] == '.':
                dp[i][j] = dp[i - 1][j]
            if i > 0 and j > 0 and matrix[i][j] == '.':
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp


if __name__ == '__main__':
    (H, W) = list(map(int, input().split(' ')))
    matrix = []
    reverse_matrix = []
    for i in range(H):
        s = input()
        matrix.append(s)
        reverse_matrix.insert(0, s[::-1])


    Q = int(input())
    dp = get_dp(matrix, H, W)
    reverse_dp = get_dp(reverse_matrix, H, W)

    for _ in range(Q):
        i, j = map(int, input().split(' '))
        print(solution(matrix, dp, reverse_dp, i, j, H, W))


