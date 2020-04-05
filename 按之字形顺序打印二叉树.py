#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   按之字形顺序打印二叉树.py
@Time    :   2020/04/05 13:59:29
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
             第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行
             以此类推。
"""
from collections import deque

# https://www.nowcoder.com/practice/91b69814117f4e8097390d107d2efbe0


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    使用两个辅助栈，在打印某一层结点是，把下一层的子节点保存到相应的栈里。
    如果当前打印的是奇数层，则先保存左子节点再保存右子节点到第一个栈里；
    如果当前打印的是偶数层，则先保存右子节点再保存左子节点到第二个栈里。
    """
    def Print(self, pRoot):
        if not pRoot:
            return []

        levels = [deque(), deque()]
        cur, next = 0, 1
        res, tmp = [], []
        levels[cur].append(pRoot)
        while len(levels[0]) or len(levels[1]):
            node = levels[cur].pop()
            tmp.append(node.val)
            if cur == 0:
                if node.left:
                    levels[next].append(node.left)
                if node.right:
                    levels[next].append(node.right)
            else:
                if node.right:
                    levels[next].append(node.right)
                if node.left:
                    levels[next].append(node.left)
            if len(levels[cur]) == 0:
                cur = 1 - cur
                next = 1 - next
                res.append(tmp)
                tmp = []
        return res
