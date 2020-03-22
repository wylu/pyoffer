#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   合并两个排序的链表.py
@Time    :   2020/03/22 19:38:01
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要
             合成后的链表满足单调不减规则。
"""

# https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337


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

    @classmethod
    def tolist(cls, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        head = ListNode(0)
        cur = head
        while pHead1 or pHead2:
            if not pHead1:
                cur.next = pHead2
                break
            if not pHead2:
                cur.next = pHead1
                break
            if pHead1.val < pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur = cur.next
        return head.next


if __name__ == '__main__':
    l1, l2 = ListNode.mklist(1, 3, 5), ListNode.mklist(2, 4, 6)
    print(ListNode.tolist(Solution().Merge(l1, l2)))
