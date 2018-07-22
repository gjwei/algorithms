# coding: utf-8
# Author: gjwei
"""
https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/
"""

class BSTNode():
    def __init__(self, val):
        self.val = val
        self.left_count = 0
        self.dup = 1
        self.left, self.right = None, None


def count_smaller(nums):
    if len(nums) == 0:
        return []
    