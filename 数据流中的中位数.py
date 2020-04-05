#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   数据流中的中位数.py
@Time    :   2020/04/05 16:40:36
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数
             就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么
             中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读
             取数据流，使用GetMedian()方法获取当前读取数据的中位数。
"""
from heapq import *

# https://www.nowcoder.com/practice/9be0172896bd43948f8a32fb954e1be1


class Solution:
    """
    把整个数据分成两部分，max(第一部分) <= min(第二部分)。
    第一部分用最大堆存储，第二部分用最小堆存储。
    """
    def __init__(self):
        self.maxh = []
        self.minh = []

    def Insert(self, num):
        heappush(self.minh, -heappushpop(self.maxh, num))
        if len(self.minh) > len(self.maxh):
            heappush(self.maxh, -heappop(self.minh))

    def GetMedian(self, s):
        if len(self.maxh) > len(self.minh):
            return self.maxh[0]
        return (self.maxh[0] + (-self.minh[0])) / 2.0


# if __name__ == '__main__':
#     solu = Solution()
#     for e in [5, 2, 3, 4, 1, 6, 7, 0, 8]:
#         solu.Insert(e)
#         print(solu.GetMedian(0), end=' ')
#     print()
