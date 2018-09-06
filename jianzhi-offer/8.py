# coding: utf-8

# 旋转数组最小值

def find_min(nums):
    left, right = 0, len(nums) - 1
    while left < right and nums[left] > nums[right]:
        mid = (left + right) >> 1
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


if __name__ == '__main__':
    nums = [5, 6, 7, 1]
    print(find_min(nums))