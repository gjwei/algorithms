# coding: utf-8

# 二维数组的查找
def search_2d_array(array, target):
    n = len(array)
    if n == 0:
        return -1
    
    m = len(array[0])

    row, col = 0, m - 1

    while row < n and col >= 0:
        if array[row][col] > target:
            col -= 1
        elif array[row][col] < target:
            row += 1
        else:
            return array[row][col]
    return -1