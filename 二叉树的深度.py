#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   二叉树的深度.py
@Time    :   2020/03/30 22:23:37
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点
             （含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
"""

# https://www.nowcoder.com/practice/435fb86331474282a3499955f0a41e8b


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """深度优先遍历"""
    @classmethod
    def deep(cls, root):
        if not root:
            return 0
        ld = Solution.deep(root.left)
        rd = Solution.deep(root.right)
        return ld + 1 if ld > rd else rd + 1

    def TreeDepth(self, pRoot):
        return Solution.deep(pRoot)
