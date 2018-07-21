# coding: utf-8
# Author: gjwei
"""问题：Larget Rectangle
https://leetcode.com/problems/largest-rectangle-in-histogram/description/
"""

def laygestRectangleArea(height):
    n = len(height)
    gmax = -(1 << 30)
    stack = []
    for i in range(n):
        while stack and height[stack[-1]] > height[i]:
            last = stack.pop()
            if stack:
                # i - 1 - s.peek() uses the starting index where height[s.peek() + 1] >= height[tp],
                # because the index on top of the stack right now is the first index left of tp with
                # height smaller than tp's height.
                area = height[last] * (i - (stack[-1] + 1))  # 左边始终有个大于当前位置的高度
            else:
                area = height[last] * i
            gmax = max(gmax, area)

        stack.append(i)
    # 当stack不为空的时候，说明从某个位置开始到最后(i = n)的位置都是非递减的。这个时候需要计算是否存在最大面积
    while stack:
        last = stack.pop()
        if len(stack) == 0:
            area = (len(height) - (stack[-1] + 1)) * height[last]  #
        else:
            area = height[last] * len(height)

        gmax = max(gmax, area)

    return gmax


"""
Longest Valid Parentheses
https://leetcode.com/problems/longest-valid-parentheses/description/
"""
def longest_valid_parenthese(s):
    stack = []
    result = 0
    for index, val in enumerate(s):
        if val == ')' and stack and s[stack[-1]] == '(':  # 此时可以统计当前的")"到最开始未能匹配的符号的位置
            stack.pop()  # 弹出可以相匹配的")"
            if not stack:
                result = max(result, index + 1)
            else:
                result = max(result, index - stack[-1])
        else:
            stack.append(index)

    return result



"""
All nearest smaller values
一个value v的左邻居是出现在v之前的数，但是小于v，而且比其他数的位置更近。
对于一个数组，求数组中所有数对应的左邻居
# 思路：
1. 最近：空间位置
2. Invariant: 维持一个严格递增的stack
3. 如果是求解larger value，就换成一个严格递减的stack
"""
def all_nearest_smaller_values(nums):
    p = [-1 for _ in nums]
    stack = []
    for i, v in enumerate(nums):
        while stack and nums[stack[-1]] >= v:
            stack.pop()
        if stack:
            p[i] = stack[-1]
        else:
            p[i] = -1
        stack.append(i)
    return p