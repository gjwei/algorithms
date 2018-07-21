# coding: utf-8
# Author: gjwei

class Node(object):
    def __init__(self, val):
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
