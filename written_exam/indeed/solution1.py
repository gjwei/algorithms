#!/usr/bin/env python
#-*- coding:utf-8 -*- 
#Author: gjwei
import sys



if __name__ == '__main__':
    N, Q = list(map(int, input().split(' ')))
    nums = list(map(int, input().split(' ')))
    even_sum = 0
    for n in nums:
        if n & 1 == 0:
            even_sum += n
    for i in range(Q):
        index, x = list(map(int, input().split(' ')))
        if nums[index - 1] & 1 == 0:  # 偶数
            if x & 1 == 0:  # 偶数
                even_sum += x
                print(even_sum)
            else:
                even_sum -= nums[index - 1]
                print(even_sum)

        else:  # nums[index - 1】qishu
            if x & 1 == 0:  # 变成奇数
                print(even_sum)
            else:
                even_sum += x + nums[index - 1]
                print(even_sum)

        nums[index - 1] += x



