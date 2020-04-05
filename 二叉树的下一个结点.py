#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   二叉树的下一个结点.py
@Time    :   2020/04/05 13:06:49
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
             注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""

# https://www.nowcoder.com/practice/9023a0c988684a53960365b889ceaf5e


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    """
    考虑三种情况：
    1.如果这个结点有右子树，那么下一个结点一定是右子树的最左结点
    2.如果这个结点没有右子树，且是父结点的左结点，则下一个结点即为父结点
    3.如果这个结点没有右子树，且是父结点的右结点，则向上循环查找，直到父结点
      是祖父结点的左结点
    """
    def GetNext(self, pNode):
        if not pNode:
            return

        if pNode.right:
            node = pNode.right
            while node.left:
                node = node.left
            return node

        if not pNode.next:
            return

        if pNode.next.left == pNode:
            return pNode.next

        if pNode.next.right == pNode:
            node = pNode.next
            while node.next and node.next.left != node:
                node = node.next
            return node.next
