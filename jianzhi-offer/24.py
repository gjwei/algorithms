# coding: utf-8

# 后续遍历二叉树

def post_order(root):
    if root is None:
        return []
    result = []
    stack = []
    p = root
    while stack or p:
        if p:
            stack.append(p)
            result.insert(0, p.val)
            p = p.right
        else:
            t = stack.pop()
            p = t.right
    return result