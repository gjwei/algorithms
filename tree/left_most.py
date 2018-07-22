# coding: utf-8
# Author: gjwei
"""Find the left most node"""
def leftmost(root):
    """层序遍历，找到每一层的left node"""
    if root is None:
        return None
    queue = [root]
    result = []
    while queue:
        size = len(queue)
        for i in range(size):
            p = queue.pop(0)
            if i == 0:
                result.append(p.val)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
    return result







