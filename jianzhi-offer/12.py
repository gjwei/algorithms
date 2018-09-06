# coding: utf-8

# 打印1到最大的n位数

def print_n(n):
    result = []
    backtracking(n, result, [])
    return result

def backtracking(n, result, tmp):
    if len(tmp) == n:
        result.append(str_tmp(tmp))
        return

    for i in range(0, 10):
        tmp.append(str(i))
        
        backtracking(n, result, tmp)

        tmp.pop()
    return

def str_tmp(tmp):
    r = []
    for i in range(len(tmp)):
        if tmp[i] == '0' and len(r) == 0:
            continue
        else:
            r.append(tmp[i])
    return ''.join(r) or '0'

print(print_n(3))
            

