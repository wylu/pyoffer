#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   删除链表中重复的结点.py
@Time    :   2020/04/05 11:55:06
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不
             保留，返回链表头指针。例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""

# https://www.nowcoder.com/practice/fc533c45b73a41b0b44ccba763f866ef


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # @classmethod
    # def prt(cls, head):
    #     if head:
    #         print(head.val, end='')
    #         head = head.next
    #     while head:
    #         print('->' + str(head.val), end='')
    #         head = head.next
    #     print()

    # @classmethod
    # def mk(cls, *args):
    #     head = ListNode(0)
    #     node = head
    #     for val in args:
    #         node.next = ListNode(val)
    #         node = node.next
    #     return head.next


class Solution:
    """
    1.为连接添加一个头结点，方便处理原头结点就是重复结点的情况
    2.遍历链表，记录当前结点的前一个结点
    3.如果当前结点是一个重复结点，找到重复结点的尾结点
    4.将当前结点的上一个结点指向重复结点尾结点的下一个结点
    """
    def deleteDuplication(self, pHead):
        if not pHead or not pHead.next:
            return pHead

        ahead = ListNode(0)
        ahead.next = pHead
        pre, cur = ahead, pHead

        while cur:
            post = cur
            if post.next and post.next.val == cur.val:
                while post.next and post.next.val == cur.val:
                    post = post.next
                pre.next = post.next
                post.next = None
                del cur
                cur = pre.next
            else:
                pre = cur
                cur = cur.next

        return ahead.next


# if __name__ == '__main__':
#     link_list = ListNode.mk(1, 2, 3, 3, 4, 4, 5)
#     ListNode.prt(link_list)
#     ListNode.prt(Solution().deleteDuplication(link_list))

#     link_list = ListNode.mk(1)
#     ListNode.prt(link_list)
#     ListNode.prt(Solution().deleteDuplication(link_list))
