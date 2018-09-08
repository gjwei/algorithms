# coding: utf-8

# 判断字符串是否是回文

def is_palindrome(s):
    if len(s) == 0:
        return True
    
    left, right = 0, len(s) - 1
    while left < right:
        if not is_alpha(s[left]):
            left += 1
        elif not is_alpha(s[right]):
            right -= 1
        elif s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1

    return True


def is_alpha(c):
    return 'a' <= c <= 'z' or 'A' <= c <= 'Z'
