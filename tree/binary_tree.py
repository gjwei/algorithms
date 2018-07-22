# coding: utf-8
# Author: gjwei
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def max_depth(node):
    if node is None:
        return 0
    return max(max_depth(node.left), max_depth(node.right)) + 1


def max_depth_2(node, depth):
    if node is None:
        return depth
    return max(max_depth_2(node.left, depth + 1),
               max_depth_2(node.right, depth + 1))


def min_depth(node, depth):
    if node is None:
        return depth
    if node.left is None and node.right:
        return min_depth(node.right, depth + 1)
    elif node.right is None and node.left:
        return min_depth(node.left, depth + 1)
    return min(min_depth(node.left, depth + 1),
               min_depth(node.right, depth + 1))


def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1


"""Construct path from root to a target"""
def construct_path(root, target, path, found):
    if root is None:
        return
    if found[0]:
        return
    path.append(root)
    if root == target:
        found[0] = True
    construct_path(root.left, target, path, found)
    construct_path(root.right, target, path, found)
    if not found[0]:
        path.pop()


"""Lowest common ancestor"""
def lca(root, n1, n2):
    if root is None:
        return None
    if root == n1 or root == n2:
        return root
    left = lca(root.left, n1, n2)
    right = lca(root.right, n1, n2)
    if left and right:
        return root
    return left or right




