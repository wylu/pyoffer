#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   链表中环的入口结点.py
@Time    :   2020/04/04 18:55:45
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""

# https://www.nowcoder.com/practice/253d2c59ec3e4bc68da16833f79a38e4


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    1.快慢指针判断链表是否有环
    2.计算环结点数目，记为n
    3.两个指针指向头结点，其中一个指针先走n步，然后两个指针同时前进，直到它们相遇
    """
    def EntryNodeOfLoop(self, pHead):
        if not pHead or not pHead.next:
            return

        p1, p2 = pHead, pHead.next.next
        while p2 and p2.next and p2 != p1 and p2.next != p1:
            p1 = p1.next
            p2 = p2.next.next

        loop = p2 == p1 or p2.next == p1
        if not loop:
            return

        cnt = 1
        p1 = p2
        while p2.next != p1:
            p2 = p2.next
            cnt += 1

        p1, p2 = pHead, pHead
        for _ in range(0, cnt):
            p2 = p2.next

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1


if __name__ == '__main__':
    head = ListNode(1)
    node = head
    node.next = ListNode(2)
    node = node.next
    node.next = ListNode(3)
    node = node.next
    loop = node
    node.next = ListNode(4)
    node = node.next
    node.next = ListNode(5)
    node = node.next
    node.next = ListNode(6)
    node = node.next
    node.next = loop
    print(Solution().EntryNodeOfLoop(head).val)
