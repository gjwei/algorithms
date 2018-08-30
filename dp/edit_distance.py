# coding: utf-8
# Author: gjwei

def edit_distance(s1, s2):
    dp = [[0 for _ in range(len(s1)+ 1) ] for _ in range(len(s2) + 1)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j]
            else:
                dp[i + 1][j + 1] = min(dp[i][j + 1],  # delete
                                       dp[i + 1][j],  # insert
                                        dp[i][j]) + 1  # replace
    return dp[len(s2)][len(s1)]
