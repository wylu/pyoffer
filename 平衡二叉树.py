#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   平衡二叉树.py
@Time    :   2020/03/30 22:34:06
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入一棵二叉树，判断该二叉树是否是平衡二叉树。
"""

# https://www.nowcoder.com/practice/8b3b95850edb4115918ecebdf1b4d222


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    深度优先遍历
    递归地比较左、右子树的高度差，若大于1，则返回 False；否则返回 True
    """
    @classmethod
    def balance(cls, root, depth):
        if not root:
            depth[0] = 0
            return True

        ld, rd = [0], [0]
        if Solution.balance(root.left, ld) and Solution.balance(
                root.right, rd):
            if abs(ld[0] - rd[0]) <= 1:
                depth[0] += max(ld[0], rd[0]) + 1
                return True
        return False

    def IsBalanced_Solution(self, pRoot):
        return Solution.balance(pRoot, [0])
