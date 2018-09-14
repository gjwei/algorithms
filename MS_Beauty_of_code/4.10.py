# coding: utf-8


def find_magic_nums():
    result = []
    is_visited = [False for _ in range(9)]
    backtracking([], is_visited, result)
    return result


def backtracking(r, is_visited, results):
    if len(r) == 9:
        results.append(''.join(r))
        return
    
    for i in range(9):
        if not is_visited[i] and (int(''.join(r) or '0') * 10 + i + 1) % (len(r) + 1) == 0:
            r.append(str(i + 1))
            is_visited[i] = True
            backtracking(r, is_visited, results)
            is_visited[i] = False
            r.pop()

    return


if __name__ == '__main__':
    print(find_magic_nums())