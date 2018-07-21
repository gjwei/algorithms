# coding: utf-8
# Author: gjwei

from linkedList.LinkedList import ListNode

"""得到前一个的引用"""
def get_pre(head, node):
    dummy = ListNode(0)
    dummy.next = head
    pre, cur = dummy, dummy.next
    while cur:
        if cur == node:
            return pre
        cur = cur.next
    return None

"""翻转链表
"""
def reverse_list(head):
    if head is None:
        return head

    dummy = ListNode(0)
    dummy.next = head

    left = head

    while left and left.next:
        next = left.next
        left.next = left.next.next
        next.next = dummy.next
        dummy.next = next
    return dummy.next


"""要求O(n)的解法，没有额外的空间"""
"""
判断两个lists是否有intersects
思路：如果两个lists有相交，那么肯定会在重点是intersect的。
加大点难度：求解相交的位置
"""
def list_length(head):
    result = 0
    while head:
        result += 1
        head = head.next
    return result


def list_intersection(head1, head2):
    len1 = list_length(head1)
    len2 = list_length(head2)
    # 保证head1 是要比head2长的
    if len1 < len2:
        head1, head2 = head2, head1
        len1, len2 = len2, len1

    gap = len1 - len2
    while gap > 0:
        head1 = head1.next
        gap -= 1
    while head1 and head2:
        if head1 == head2:
            return head1
        head1 = head1.next
        head2 = head2.next
    return None

"""
Determine whether the list is palindrome
判断一个list是否是回文
思路：先翻转，在进行判断
"""


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        half = slow
        half = self.reverse_list(half)
        p, q = head, half
        while p and q:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next

        return True

    def reverse_list(self, head):
        dummy = ListNode(0)
        dummy.next = head
        left = head
        while left and left.next:
            next = left.next
            left.next = left.next.next
            next.next = dummy.next
            dummy.next = next
        return dummy.next




def print_link_list(head):
    result = []
    p = head
    while p:
        result.append(str(p.val))
        p = p.next
    print(' '.join(result))

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    reverse_head = reverse_list(head)
    print_link_list(reverse_head)


