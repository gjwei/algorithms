# coding: utf-8


def queens(n):
    result = []
    cols = [i for i in range(n)]
    _queens(result, cols, 0, n)
    return result


def _queens(result, cols, index, n):

    if index == n:
        result.append(cols[:])
        return
    for row in range(n):
        if is_valid(cols, index, row):
            cols[index] = row
            _queens(result, cols, index + 1, n)
    return


def is_valid(cols, index, row):
    for i in range(index):
        row2 = cols[i]
        if row2 == row or abs(row2 - row) == index - i:
            return False
    return True


if __name__ == '__main__':
    print(queens(8))
