# coding: utf-8

def power(num, k):
    if k < 0:
        return 1 / power(nums, -k)
    result = 1
    while k > 0:
        if k & 1 == 1:
            result *= num
            k -= 1
        else:
            result *= result
            k //= 2
    
    return result


print(power(5, 3))
