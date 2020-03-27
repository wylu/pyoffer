#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   二叉搜索树与双向链表.py
@Time    :   2020/03/27 21:41:05
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
             要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""

# https://www.nowcoder.com/practice/947f6eb80d944a84850b0538bf0ec3a5


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    把树看成3部分，左子树、根结点和右子树。利用一个指针记录当前双向链表的尾结点，
    在中序遍历的过程中，将当前访问的结点链接到尾结点，并更新尾结点指针。
    """
    @classmethod
    def convert(cls, root, tail):
        if not root:
            return

        cur = root
        Solution.convert(cur.left, tail)

        cur.left = tail[0]
        if tail[0]:
            tail[0].right = cur
        tail[0] = cur

        Solution.convert(cur.right, tail)

    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        # tail 指向双向链表尾结点
        tail = [None]
        Solution.convert(pRootOfTree, tail)

        head = tail[0]
        while head.left:
            head = head.left
        return head
