# coding: utf-8
# Author: gjwei

def solution(nums, k):
    nums = sorted(nums)

    expired_day = 0
    result = 0
    index = 0

    while index < len(nums):
        for i in range(k):
            if i + index < len(nums) and nums[index + i] > expired_day:
                result += 1

        index += k

        expired_day += 1
    return result


import sys

if __name__ == '__main__':
    t = int(sys.stdin.readline().strip())

    for _ in range(t):
        n, k = list(map(int, sys.stdin.readline().strip().split()))
        nums = list(map(int, sys.stdin.readline().strip().split()))
        print(solution(nums, k))




