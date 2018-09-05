# coding: utf-8

def single_number2(nums):
    # Given a non-empty array of integers, every 
    # element appears three times except for one, 
    # which appears exactly once. Find that single one.
    counts = [0 for _ in range(32)]
    for n in nums:
        for i in range(32):
            counts[i] += (n >> (31 - i)) & 1

    result = 0
    for i in range(32):
        if counts[i] % 3 != 0:
            result += (1 << i)

    return result    

    
    


