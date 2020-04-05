#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   把二叉树打印成多行.py
@Time    :   2020/04/05 14:53:47
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""
from collections import deque

# https://www.nowcoder.com/practice/445c44d982d04483b04a54f298796288


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []

        queue, res, tmp = deque(), [], []
        cl, nl = pRoot, None
        queue.append(pRoot)
        while len(queue):
            node = queue.popleft()
            tmp.append(node.val)
            if node.left:
                queue.append(node.left)
                nl = node.left
            if node.right:
                queue.append(node.right)
                nl = node.right
            if node == cl:
                res.append(tmp)
                tmp = []
                cl, nl = nl, cl
        return res
