#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   二叉树中和为某一值的路径.py
@Time    :   2020/03/26 22:42:50
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
             路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在
             返回值的list中，数组长度大的数组靠前)
"""

# https://www.nowcoder.com/practice/b736e784e3e34731af99065031301bca


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    当用前序遍历的方式访问到某一结点时，把该结点添加到路径上，并累加该结点的值。
    如果该结点为叶结点，且路径中结点值的和刚好等于目标的和，则当前路径符合要求，
    把该路径添加到结果数组中；如果当前结点不是叶结点，则继续访问它的子节点。

    当前结点访问结束后，递归函数将自动回到它的父结点。因此我们在函数退出之前要在
    路径上删除当前结点并减去当前结点的值，以确保返回父结点时路径刚好是从根结点到
    父结点。
    """
    @classmethod
    def find(cls, res, root, target, cur, path):
        path.append(root.val)
        cur += root.val

        if root.left:
            Solution.find(res, root.left, target, cur, path)
        if root.right:
            Solution.find(res, root.right, target, cur, path)

        if not root.left and not root.right:
            if cur == target:
                res.append(path[:])

        path.pop()

    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        res = []
        if not root:
            return res
        Solution.find(res, root, expectNumber, 0, [])
        return res
