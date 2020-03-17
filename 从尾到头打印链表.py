#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   从尾到头打印链表.py
@Time    :   2020/03/17 11:27:55
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
"""

# https://www.nowcoder.com/practice/d0267f7f55b3412ba93bd35cfa8e8035


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.res = []

    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return self.res
        if listNode.next:
            self.printListFromTailToHead(listNode.next)
        self.res.append(listNode.val)
        return self.res

    @classmethod
    def make_list(cls, src):
        head = ListNode(0)
        cur = head
        for num in src:
            cur.next = ListNode(num)
            cur = cur.next
        return head.next


if __name__ == '__main__':
    link_list = Solution.make_list([3, 2, 1])
    print(Solution().printListFromTailToHead(link_list))
