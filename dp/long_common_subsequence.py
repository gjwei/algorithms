# coding: utf-8
# Author: gjwei

def lcs_v1(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return 0
    if s1[0] == s2[0]:
        return 1 + lcs_v1(s1[1:], s2[1:])
    else:
        return max(lcs_v1(s1, s2[1:]), lcs_v1(s1[1:], s2))

def lcs_dp(s1, s2):
    dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[len(s1)][len(s2)]


if __name__ == '__main__':
    s1 = 'abcd'
    s2 = 'acd'
    print(lcs_dp(s1, s2))