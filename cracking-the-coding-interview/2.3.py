# coding: utf-8

def remove_node(node):
    if node is None:
        return 
    
    if node.next is None:
        del node
        return

    node.val = node.next.val
    node.next = node.next.next
    return