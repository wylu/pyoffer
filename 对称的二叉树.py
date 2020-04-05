#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   对称的二叉树.py
@Time    :   2020/04/05 13:33:07
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树
             同此二叉树的镜像是同样的，定义其为对称的。
"""

# https://www.nowcoder.com/practice/ff05d44dfdb04e1d83bdbdab320efbcb


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    1.定义一种与前序遍历对称的遍历算法，即先访问右结点，再访问根结点，最后访问左结点
    2.用这两种算法同时遍历二叉树，如果当前访问结点不相等，则返回false；如果直到遍历
      结束都相等，则返回true。（需要考虑左右子节点为空的情况）
    """
    @staticmethod
    def symmetrical(lroot, rroot):
        if not lroot and not rroot:
            return True
        if not lroot or not rroot:
            return False
        if lroot.val != rroot.val:
            return False
        return (Solution.symmetrical(lroot.left, rroot.right)
                and Solution.symmetrical(lroot.right, rroot.left))

    def isSymmetrical(self, pRoot):
        return Solution.symmetrical(pRoot, pRoot)
