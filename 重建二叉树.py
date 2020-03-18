#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   重建二叉树.py
@Time    :   2020/03/18 09:30:50
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入
             的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列
             {1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树
             并返回。
"""

# https://www.nowcoder.com/practice/8a19cbe657394eeaac2f6ea9b0f6fcf6


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.pre = None
        self.tin = None

    def construnct(self, start_pre, end_pre, start_tin, end_tin):
        if start_pre == end_pre:
            return None
        root = TreeNode(self.pre[start_pre])
        i = start_tin
        while self.tin[i] != root.val and i < end_tin:
            i += 1
        llen = i - start_tin  # 左子树序列长度
        mpre = start_pre + 1 + llen  # 左右子树序列中点（右子树序列起始点）
        root.left = self.construnct(start_pre + 1, mpre, start_tin, i - 1)
        root.right = self.construnct(mpre, end_pre, i + 1, end_tin)
        return root

    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin or len(pre) != len(tin):
            return
        self.pre, self.tin = pre, tin
        return self.construnct(0, len(pre), 0, len(tin))
