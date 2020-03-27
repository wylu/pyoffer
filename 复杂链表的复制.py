#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   复杂链表的复制.py
@Time    :   2020/03/27 20:40:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
             另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
             （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""

# https://www.nowcoder.com/practice/f836b2c43afc4b35ad6adc41ec941dba


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    """
    第一步根据原链表的每个结点 N 复制对应的 N'，把 N' 链接在 N 的后面，如：
    原链表：Ａ－> B -> C -> D -> E
    复制后：Ａ -> A' -> B -> B' -> C -> C' -> D -> D' -> E -> E'

    第二步设置复制结点的 random 域，假设原链表的 N 的 random 指向 S，那么
    其对应复制结点 N' 是 N 的 random 指向的结点，同样 S' 也是 S 的 random
    指向的结点。

    第三步将这个长链表拆分两个链表。
    """

    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None

        cur = pHead
        # Step 1
        while cur:
            node = RandomListNode(cur.label)
            node.next = cur.next
            cur.next = node
            cur = node.next

        cur = pHead
        # Step 2
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        cur = pHead
        res = cur.next
        # Step 3
        while cur:
            tmp = cur.next
            cur.next = tmp.next
            cur = cur.next
            if cur:
                tmp.next = cur.next
        return res
