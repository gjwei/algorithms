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