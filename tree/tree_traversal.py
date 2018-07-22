# coding: utf-8
# Author: gjwei
"""
https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45551/Preorder-Inorder-and-Postorder-Iteratively-Summarization
"""
def inorder_recursive(root, result):
    if root is None:
        return
    inorder_recursive(root.left, result)
    result.append(root.val)
    inorder_recursive(root.right, result)


def inorder_non_recursize(root):
    result = []
    if root is None:
        return []
    stack = []
    p = root
    while p or stack:
        if p:
            stack.append(p)
            p = p.left
        else:
            q = stack.pop()
            result.append(q.val)
            p = q.right
    return result


def preorder_non_recursive(root):
    result = []
    if root is None:
        return result
    stack, p = [], root
    while stack or p:
        if p:
            stack.append(p)
            result.append(p.val)
            p = p.left
        else:
            q = stack.pop()
            p = q.right
    return result


def postorder_non_recursive(root):
    result = []
    if root is None:
        return result
    stack, p = [], root
    while p or stack:
        if p:
            stack.append(p)
            result.insert(0, p.val)
            p = p.right
        else:
            q = stack.pop()
            p = q.left
    return result


def level_order(root):
    result, queue = [], [root]
    if root is None:
        return result

    while queue:
        size = len(queue)
        for _ in range(size):
            t = queue.pop(0)
            result.append(t.val)
            if t.left:
                queue.append(t.left)
            if t.right:
                queue.append(t.right)
    return result
