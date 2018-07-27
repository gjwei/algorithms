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


"""d对于含有大量重复的数组，可以采用三相切分方法"""

def threeway_quicksort(nums, low, high):
    if high <= low:
        return
    lt, i, gt = low, low + 1, high
    v = nums[low]
    while i <= gt:
        cmp = nums[i] - v
        if cmp < 0:
            nums[lt], nums[i] = nums[i], nums[lt]
            lt += 1
            i += 1
        elif cmp > 0:
            nums[i], nums[gt] = nums[gt], nums[i]
            gt -= 1
        else:
            i += 1
    threeway_quicksort(nums, low, lt - 1)
    threeway_quicksort(nums, gt + 1, high)

if __name__ == '__main__':
    a = [4, 2, 2,5, 1, 1, 1, 1]
    print(quick_sort(a))