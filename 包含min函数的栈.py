#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   包含min函数的栈.py
@Time    :   2020/03/24 23:17:17
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数
             （时间复杂度应为O(1)）。
             注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法。
"""

# https://www.nowcoder.com/practice/4c776177d2c04c2494f2555c9fcc1e49


class Solution:
    """
    空间换时间，使用两个栈（一个数据栈、一个辅助栈）实现O(1)时间复杂度的min函数。
    每次将元素压入数据栈的同时，将最小元素压入辅助栈；每次数据栈弹出栈顶元素时，
    辅助栈也弹出栈顶元素。
    """
    def __init__(self):
        self.data = []
        self.mini = []

    def push(self, node):
        self.data.append(node)
        if not self.mini or node < self.mini[-1]:
            self.mini.append(node)
        else:
            self.mini.append(self.mini[-1])

    def pop(self):
        self.mini.pop()
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def min(self):
        return self.mini[-1]


if __name__ == '__main__':
    stack = Solution()
    stack.push(3)
    print(stack.min())
    stack.push(4)
    print(stack.min())
    stack.push(2)
    print(stack.min())
    stack.push(1)
    print(stack.min())
