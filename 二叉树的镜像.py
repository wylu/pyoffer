#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   二叉树的镜像.py
@Time    :   2020/03/24 22:02:00
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   操作给定的二叉树，将其变换为源二叉树的镜像。

二叉树的镜像定义：

        源二叉树
            8
           /  \
          6   10
         / \  / \
        5  7 9  11

        镜像二叉树
            8
           /  \
          10   6
         / \  / \
        11 9 7   5
"""

# https://www.nowcoder.com/practice/564f4c26aa584921bc75623e48ca3011


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @classmethod
    def new_mirror(cls, root):
        """构造一棵新的镜像二叉树"""
        if not root:
            return None
        mrt = TreeNode(root.val)
        mrt.left = Solution.new_mirror(root.right)
        mrt.right = Solution.new_mirror(root.left)
        return mrt

    @classmethod
    def old_mirror(cls, root):
        """直接在原树上修改"""
        if not root:
            return None
        root.left, root.right = root.right, root.left
        Solution.old_mirror(root.left)
        Solution.old_mirror(root.right)

    # 返回镜像树的根节点
    def Mirror(self, root):
        return Solution.old_mirror(root)
