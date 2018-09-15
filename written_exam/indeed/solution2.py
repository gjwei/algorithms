#!/usr/bin/env python
#-*- coding:utf-8 -*- 
#Author: gjwei
import sys
def solution(nums):
    if len(nums) == 0 or len(nums) == 1:
        return 0

    stack = []
    for i in range(len(nums)):
        if i == 0:stack.append(i)
        else:
            if nums[i] > nums[stack[-1]]:





    return result


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split(' ')))


    print(solution(nums))



