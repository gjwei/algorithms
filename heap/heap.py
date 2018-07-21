# coding: utf-8
# Author: gjwei
class Heap(object):
    def __init__(self, nums):
        self.heap = nums

    def sink(self, index):
        """Compare parent to the larger child"""
        while 2 * index < len(self.heap):
            c = 2 * index
            if c + 1 <