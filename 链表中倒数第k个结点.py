#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   链表中倒数第k个结点.py
@Time    :   2020/03/22 19:00:32
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入一个链表，输出该链表中倒数第k个结点。
"""

# https://www.nowcoder.com/practice/529d3ae5a407492994ad2a246518148a


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def mklist(cls, *args):
        head = ListNode(0)
        cur = head
        for val in args:
            cur.next = ListNode(val)
            cur = cur.next
        return head.next


class Solution:
    """
    为了实现只遍历链表一次就能找到倒数的第k个结点，我们可以定义两个指针。
    第一个指针从链表的头指针开始遍历向前走k-1步，第二个指针保持不动；从第
    k步开始，第二个指针也开始从链表的头指针开始遍历。由于两个指针的距离保
    持在k-1，当第一个（走在前面的）指针到达链表的尾结点时，第二个（走在后
    面的）指针正好指向倒数第k个结点。
    """
    def FindKthToTail(self, head, k):
        if k <= 0:
            return None
        try:
            p1, p2 = head, head
            for _ in range(k - 1):
                p1 = p1.next
            while p1.next:
                p1 = p1.next
                p2 = p2.next
            return p2
        except AttributeError:
            return None


if __name__ == '__main__':
    print(Solution().FindKthToTail(ListNode.mklist(1, 2, 3, 4, 5), 2).val)
    print(Solution().FindKthToTail(ListNode.mklist(1), 1).val)
    print(Solution().FindKthToTail(ListNode.mklist(1), 100))
