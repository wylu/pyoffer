#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   序列化二叉树.py
@Time    :   2020/04/05 15:00:49
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   请实现两个函数，分别用来序列化和反序列化二叉树。二叉树的序列化是指：把一棵
             二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来
             的二叉树可以持久保存。序列化可以基于先序、中序、后序、层序的二叉树遍历方式
             来进行修改，序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），
             以 ！ 表示一个结点值的结束（value!）。二叉树的反序列化是指：根据某种遍历
             顺序得到的序列化字符串结果str，重构二叉树。
"""

# https://www.nowcoder.com/practice/cf7e25aa97c04cc1a68c8f040e71fb84


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    根据前序遍历的顺序来序列化二叉树，因为前序遍历是从根结点开始，那么相应的反序列化
    在根结点的数值读出来的时候就可以开始了。在遍历二叉树碰到空指针时，这些空指针序列
    化为一个特殊的字符（如'$'），另外结点的数值之间要用一个特殊的字符（如','）隔开。
    """
    @staticmethod
    def serial(root, res):
        if not root:
            return
        res.append(str(root.val))
        if root.left:
            Solution.serial(root.left, res)
        else:
            res.append('$')
        if root.right:
            Solution.serial(root.right, res)
        else:
            res.append('$')

    def Serialize(self, root):
        res = []
        Solution.serial(root, res)
        return ','.join(res)

    @staticmethod
    def deserial(seq, cur):
        if cur[0] == len(seq):
            return
        if seq[cur[0]] == '$':
            cur[0] += 1
            return
        root = TreeNode(int(seq[cur[0]]))
        cur[0] += 1
        root.left = Solution.deserial(seq, cur)
        root.right = Solution.deserial(seq, cur)
        return root

    def Deserialize(self, s):
        if not s:
            return
        return Solution.deserial(s.split(','), [0])


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    solu = Solution()
    seq = solu.Serialize(root)
    print(seq)

    root = solu.Deserialize(seq)
    print(solu.Serialize(root))
