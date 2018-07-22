# coding: utf-8
# Author: gjwei
def diameter_of_tree(root):
    result = [0]
    _ = max_depth(root, result)
    return result[0]

def max_depth(root, result):
    if root is None:
        return 0
    left = max_depth(root.left, result)
    right = max_depth(root.right, result)
    result[0] = max(result[0], left + right + 1)
    return max(left, right) + 1