#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   滑动窗口的最大值.py
@Time    :   2020/04/07 22:07:52
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入
             数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最
             大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
             {[2,3,4],2,6,2,5,1}，{2,[3,4,2],6,2,5,1}，{2,3,[4,2,6],2,5,1}，
             {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
"""
from collections import deque

# https://www.nowcoder.com/practice/1624bc35a45c42c0bc17d17fa0cba788


class Solution:
    """
    使用一个双端队列来保存有可能是滑动窗口最大值的数字的下标。
    1.在存入一个数字的下标之前，首先判断队列里已有数字是否小于待存入的数字。
    2.如果已有的数字小于待存入的数字，那么这些数字已经不可能是滑动窗口的最大值，
      将它们依次从队列的尾部删除。
    3.如果队列头部的数字已经从窗口里滑出，那么滑出的数字也需要从队列头部删除。
    """
    def maxInWindows(self, num, size):
        if not num or size < 1 or size > len(num):
            return []

        queue = deque()
        for i in range(0, size):
            while len(queue) > 0 and num[i] > num[queue[-1]]:
                queue.pop()
            queue.append(i)

        res = [num[queue[0]]]

        for i in range(size, len(num)):
            while len(queue) > 0 and num[i] > num[queue[-1]]:
                queue.pop()
            queue.append(i)
            if queue[0] <= i - size:
                queue.popleft()
            res.append(num[queue[0]])

        return res


if __name__ == '__main__':
    print(Solution().maxInWindows([2, 3, 4, 2, 6, 2, 5, 1], 3))
    print(Solution().maxInWindows([10, 14, 12, 11], 5))
