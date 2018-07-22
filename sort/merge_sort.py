# coding: utf-8
# Author: gjwei
def merge_sort_recursive(nums):
    if len(nums) <= 1:
        return nums
    half = len(nums) >> 1
    left_part, right_part = merge_sort_recursive(nums[:half]), merge_sort_recursive(nums[half:])
    result = merge(left_part, right_part)
    return result


def merge(left_part, right_part):
    result = []
    i, j = 0, 0
    while i < len(left_part) and j < len(right_part):
        if left_part[i] < right_part[j]:
            result.append(left_part[i])
            i += 1
        else:
            result.append(right_part[j])
            j += 1
    result += left_part[i:] + right_part[j:]
    return result

# inplace merge
def merge_sort_iteration(nums):
    n, unit = len(nums), 1
    while unit <= len(nums):
        for i in range(0, n, unit * 2):
            lo, hi = i, min(n, i + 2 * unit)
            mid = i + unit
            p, q = lo, mid
            while p < mid and q < hi:
                if nums[p] < nums[q]:
                    p += 1
                else:
                    tmp = nums[q]
                    nums[p + 1: q + 1] = nums[p: q]
                    nums[p] = tmp
                    p, mid, q = p + 1, mid + 1, q + 1
        unit *= 2
    return nums




if __name__ == '__main__':
    a = [2, 4, 1, 2, 4]
    print(merge_sort_iteration(a))
