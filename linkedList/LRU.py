# coding: utf-8
# Author: gjwei

class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre, self.next = None, None


class LRUCache(object):
    """
    LRU chche function(least recently used cache)
    1. Ensure O(1) find O(1) deletion.
    2. Doubly linked list + map.
    3. Keep both head and tail pointer.
    4. Operations on doubly linked list are case by case.
    """

    def __init__(self, capacity):
        self.capactiy = capacity
        self.map = {}
        self.head = None
        self.tail = None

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            val = node.val
            # 将节点放置到tail位置
            self.set_to_tail(node)
            return val
        return -1

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.set_to_tail(node)
        else:
            if len(self.map) < self.capactiy:
                node = Node(key, value)
                self.map[key] = node
                # set to tail or head
                if self.head is None:
                    self.head = node
                elif self.tail is None:
                    self.tail = node
                else:
                    node.pre = self.tail
                    self.tail.next = node
                    self.tail = node
            else:
                # 将head清空掉
                head_key = self.head.key
                self.map.pop(head_key)
                self.head = self.head.next
                self.head.pre = None
                node = Node(key, value)
                self.map[key] = node
                self.tail.next = node
                node.pre = self.tail
                self.tail = node
        return



    def set_to_tail(self, node):
        pre = node.pre
        next = node.next
        pre.next = next
        next.pre = pre
        self.tail.next = node
        node.pre = self.tail
        self.tail = node
        return


