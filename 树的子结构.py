#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   树的子结构.py
@Time    :   2020/03/22 22:42:45
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入两棵二叉树A，B，判断B是不是A的子结构。
             （ps：我们约定空树不是任意一个树的子结构）
"""

# https://www.nowcoder.com/practice/6e196c44c7004d15b1610b9afca8bd88


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    要查找树A中是否存在和树B结构一样的子树，我们可以分成两步：
    第一步，在树A中找到和树B的根结点的值一样的结点R;
    第二步，判断树A中以R为根结点的子树是不是包含和树B一样的结构；
    """
    @classmethod
    def has(cls, r1, r2):
        if not r1 and r2:
            return False
        if not r2:
            return True
        if r1.val != r2.val:
            return False
        return Solution.has(r1.left, r2.left) and Solution.has(
            r1.right, r2.right)

    @classmethod
    def subtree(cls, r1, r2):
        flag = False
        if not r1 or not r2:
            return flag
        if r1.val == r2.val:
            flag = Solution.has(r1.left, r2.left) and Solution.has(
                r1.right, r2.right)
        if not flag:
            flag = Solution.subtree(r1.left, r2)
        if not flag:
            flag = Solution.subtree(r1.right, r2)
        return flag

    def HasSubtree(self, pRoot1, pRoot2):
        return Solution.subtree(pRoot1, pRoot2)
