# coding: utf-8

# 移除未排序链表的重复节点

def remove_duplicate(head):
    d = set()

    p = head
    while p and p.next:
        if p.next in d:
            # remove p.next
            p.next = p.next.next
        else:
            d.add(p)
        p = p.next

    return