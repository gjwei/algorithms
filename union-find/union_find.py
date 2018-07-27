# coding: utf-8
# Author: gjwei
def union(p, q, fathers):
    p_root = find(p, fathers)
    q_root = find(q, fathers)
    if p_root != q_root:
        fathers[p_root] = q_root


def find(p, fathers):
    while p != fathers[p]:
        p = fathers[p]
    return p