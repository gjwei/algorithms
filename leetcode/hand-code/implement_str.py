# coding: utf-8

# 返回needle在haystack中第一次出现的index
def strstr(haystack, needle):
    for i in range(len(haystack) - len(needle)):
        if is_same(haystack, needle, i):
            return i
    return -1


def is_same(haystack, needle, index):
    left, right = index, index + len(needle)

    for i in range(len(needle)):
        if haystack[i + index] == needle[i]:
            continue
        else:
            return False

    return True
