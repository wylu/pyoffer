#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   两个链表的第一个公共结点.py
@Time    :   2020/03/30 00:09:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，
             所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
"""

# https://www.nowcoder.com/practice/6ab1d9a29e88450685099d45c9e31e46


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    首先遍历两个链表得到它们的长度，就能知道哪个链表比较长，以及长的链表比短的
    链表多几个结点。在第二次遍历时，在较长的链表上先走若干个步，接着同时在两个
    链表上遍历，找到的第一个相同的结点就是它们的第一个公共结点。
    """
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead1:
            return None

        len1, len2 = 0, 0
        cur1, cur2 = pHead1, pHead2
        while cur1:
            len1 += 1
            cur1 = cur1.next
        while cur2:
            len2 += 1
            cur2 = cur2.next

        cur1, cur2 = pHead1, pHead2
        if len1 > len2:
            for _ in range(len1 - len2):
                cur1 = cur1.next
        elif len1 < len2:
            for _ in range(len2 - len1):
                cur2 = cur2.next

        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next

        return cur1
