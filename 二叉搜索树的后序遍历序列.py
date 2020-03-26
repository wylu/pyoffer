#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   二叉搜索树的后序遍历序列.py
@Time    :   2020/03/26 22:10:35
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
             如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""

# https://www.nowcoder.com/practice/a861533d45854474ac791d90e447bafd


class Solution:
    """
    在后序遍历得到的序列中，最后一个数字是树的根结点的值。数组中前面的数字可以分为两部分：
    第一部分是左子树结点的值，它们都比根结点的值小；第二部分是右子树结点的值，它们都比根结
    点的值，它们都比根结点的值大。

    根据这个规律，我们可以递归地遍历左子树和右子树，以判断所有的子树是否都满足二叉搜索树的
    条件。
    """
    @classmethod
    def verify(cls, seq):
        if len(seq) <= 1:
            return True

        root = seq[-1]

        # 在二叉搜索树中左子树结点的值小于根结点的值
        i = 0
        while i < len(seq) - 1 and seq[i] <= root:
            i += 1

        # 在二叉搜索树中右子树结点的值大于根结点的值
        for j in range(i, len(seq) - 1):
            if seq[j] <= root:
                return False

        # 递归判断左子树和右子树是不是二叉搜索树
        return Solution.verify(seq[:i]) and Solution.verify(seq[i:-1])

    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        return Solution.verify(sequence)


if __name__ == '__main__':
    print(Solution().VerifySquenceOfBST([5, 7, 6, 9, 11, 10, 8]))
    print(Solution().VerifySquenceOfBST([7, 4, 6, 5]))
