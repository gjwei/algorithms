# coding: utf-8
# Author: gjwei
class Heap(object):
    """大根堆"""

    def __init__(self, nums):
        self.heap = nums

    def sink(self, index):

        while 2 * index + 1 < len(self.heap):
            c = 2 * index + 1
            # Compare parent to the larger child
            if c + 1 < len(self.heap) and self.heap[c + 1] > self.heap[c]:
                c += 1
            if self.heap[index] < self.heap[c]:
                self.heap[index], self.heap[c] = self.heap[c], self.heap[index]
                index = c
            else:
                break
        return

    def swim(self, index):
        while index > 0 and self.heap[(index - 1) // 2] < self.heap[index]:
            pi = (index - 1) >> 1
            self.heap[pi], self.heap[index] = self.heap[index], self.heap[pi]
            index = pi


# 对排序算法
def shift_down(nums, start, end):
    root = start
    while True:
        index = root * 2 + 1
        if index > end:
            break
        if index + 1 < end and nums[index + 1] > nums[index]:
            index += 1
        if nums[root] < nums[index]:
            nums[root], nums[index] = nums[index], nums[root]
            root = index
        else:
            break


def heap_sort(nums):
    # 创建大根堆
    for start in range((len(nums) - 2) >> 1, -1, -1):
        shift_down(nums, start, len(nums) -1 )

    # 堆排序
    for end in range(len(nums) - 1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]  # 将最大的数移到最后的位置
        shift_down(nums, 0, end - 1)

    return nums

# python heapq
# python only have build in min-heap

if __name__ == '__main__':
    a = [9,2,1,7,6,8,5,3,4]
    print(heap_sort(a))