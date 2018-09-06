# coding: utf-8

def find_duplicate(nums):
    if len(nums) == 0:
        return False

    for i in range(len(nums)):
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return True
            t = nums[i]
            nums[i], nums[t] = nums[t], nums[i]
    
    return False

nums = [0, 1, 4, 2, 3]
print(find_duplicate(nums))

