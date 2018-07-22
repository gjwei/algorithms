# coding: utf-8
# Author: gjwei

def quick_sort(nums):
    low, high = 0, len(nums) - 1
    _quick_sort(nums, low, high)
    return nums


def _quick_sort(nums, low, high):
    if low >= high:
        return
    pivot = partition(nums, low, high)
    _quick_sort(nums, low, pivot - 1)
    _quick_sort(nums, pivot + 1, high)
    return


def partition(nums, low, high):
    pivot = nums[high]
    index = low
    for i in range(low, high + 1):
        if nums[i] <= pivot:
            nums[index], nums[i] = nums[i], nums[index]
            index += 1
    return index - 1

if __name__ == '__main__':
    a = [4, 2, 2,5, 1, 1, 1, 1]
    print(quick_sort(a))