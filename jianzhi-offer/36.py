# coding: utf-8


def reverse_pairs(nums):
    result = []
    _ = _reverse_pairs(result, nums)
    return result


def _reverse_pairs(result, nums):
    if len(nums) == 1:
        return nums
    if len(nums) == 2:
        if nums[1] < nums[0]:
            result.append([nums[1], nums[0]])
            nums[0], nums[1] = nums[1], nums[0]
        return nums

    mid_index = (len(nums) >> 1) + 1
    left_part = _reverse_pairs(result, nums[:mid_index])
    right_part = _reverse_pairs(result, nums[mid_index:])

    new_r = []
    left_index, right_index = 0, 0
    while left_index < len(left_part) and right_index < len(right_part):
        if left_part[left_index] > right_part[right_index]:
            new_r.append(right_part[right_index])

            for index in range(left_index, len(left_part)):
                result.append([right_part[right_index], left_part[index]])

            right_index += 1
        
        else:
            new_r.append(left_part[left_index])
            left_index += 1
    
    while left_index < len(left_part):
        new_r.append(left_part[left_index])
        left_index += 1

    while right_index < len(right_part):
        new_r.append(right_part[right_index])
        right_index += 1
    
    return new_r


if __name__ == '__main__':
    nums = [7, 5, 4, 6]
    print(reverse_pairs(nums))