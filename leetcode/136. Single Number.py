# coding: utf-8

class Solution():
    def single_numbers(self, nums):
        if len(nums) == 0:
            return -1

        result = nums[0]
        for i in range(1, len(nums)):
            result ^= nums[i]
        
        return result


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 1]
    s = Solution()
    print(s.single_numbers(nums))