#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   二叉树的第k个结点.py
@Time    :   2020/04/05 15:56:41
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   给定一棵二叉搜索树，请找出其中的第k小的结点。例如（5，3，7，2，4，6，8）中，
             按结点数值大小顺序第三小结点的值为4。
"""

# https://www.nowcoder.com/practice/ef068f602dde4d28aab2b210e859150a


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def search(root, k):
        target = None
        if root.left:
            target = Solution.search(root.left, k)
        if not target:
            if k[0] == 1:
                target = root
            k[0] -= 1
        if not target and root.right:
            target = Solution.search(root.right, k)
        return target

    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if not pRoot or k == 0:
            return
        return Solution.search(pRoot, [k])


if __name__ == '__main__':
    root = TreeNode(8)
    root.left = TreeNode(6)
    root.right = TreeNode(10)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(11)
    print(Solution().KthNode(root, 1).val)
