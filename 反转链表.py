#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   反转链表.py
@Time    :   2020/03/22 19:23:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入一个链表，反转链表后，输出新链表的表头。
"""

# https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca


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
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        pl, pr = pHead, pHead.next
        pl.next = None
        while pr:
            tmp = pr.next
            pr.next = pl
            pl = pr
            pr = tmp
        return pl


if __name__ == '__main__':
    l, s = ListNode(0), Solution()
    print(l.tolist(s.ReverseList(l.mklist(1, 2, 3, 4, 5))))
    print(l.tolist(s.ReverseList(l.mklist(1, 2))))
    print(l.tolist(s.ReverseList(l.mklist(1))))
