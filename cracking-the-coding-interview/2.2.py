# coding: utf-8

def find_last_kth_node(head, k):
    p = head

    while k and p:
        p = p.next
        k -= 1
    
    if k > 0:  # list length less than k
        return None
    
    q = head

    while p and q:
        p = p.next
        q = q.next

    return p

    