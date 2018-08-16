# coding: utf-8
# Author: gjwei
def lcs_dp(s1, s2):
    """
    F(i, j) = F(i - 1, j - 1) + 1 if s1[i] == s2[j]
    \       = 0 otherwise
    """
    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    result = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                continue
            result = max(result, dp[i + 1][j + 1])
    return result
