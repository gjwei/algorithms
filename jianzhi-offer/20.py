# coding: utf-8
import ipdb

def print_matrix(matrix):
    n, m = len(matrix), len(matrix[0])

    row, col = 0, -1
    result = []

    while True:
        for j in range(m):
            col += 1
            result.append(matrix[row][col])

        n -= 1
        if n < 0:
            break

        for i in range(n):
            row += 1
            result.append(matrix[row][col])

        m -= 1
        if m < 0:
            break

        for j in range(m):
            col -= 1
            result.append(matrix[row][col])
        
        n -= 1
        if n < 0:
            break
        
        for i in range(n):
            row -= 1
            result.append(matrix[row][col])
        
        m -= 1
        if m < 0:
            break

    return result


matrix = [list(range(1, 4)), list(range(4, 7)), list(range(7, 10))]
print(matrix)
print(print_matrix(matrix))