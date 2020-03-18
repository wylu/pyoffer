#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   用两个栈实现队列.py
@Time    :   2020/03/18 23:50:26
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   用两个栈来实现一个队列，完成队列的Push和Pop操作。队列中的
             元素为int类型。
"""

# https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)
        # write code here

    def pop(self):
        if not self.stack2 and not self.stack1:
            return None
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


if __name__ == '__main__':
    queue = Solution()
    for i in [1, 2, 3]:
        queue.push(i)
    for _ in range(3):
        print(queue.pop())
