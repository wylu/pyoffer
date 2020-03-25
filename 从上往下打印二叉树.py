#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   从上往下打印二叉树.py
@Time    :   2020/03/26 00:02:10
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""
from collections import deque

# https://www.nowcoder.com/practice/7fe2212963db4790b57431d9ed259701


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """BFS"""

    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        res = []
        if not root:
            return res
        queue = deque([root])
        while len(queue):
            root = queue.popleft()
            res.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        return res
