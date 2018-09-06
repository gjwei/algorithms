# coding: utf-8

# 翻转链表
class LinkNode():
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_linkedlist(head):
    new_head = LinkNode(0)

    p = head
    while p:
        t = p
        p = p.next
        t.next = new_head.next
        new_head.next = t

    return new_head.next


def reverse_linkedlist_recursive(head):
    if head is None or head.next is None:
        return head
    
    p = reverse_linkedlist_recursive(head.next)

    head.next.next = head
    head.next = None
    return p