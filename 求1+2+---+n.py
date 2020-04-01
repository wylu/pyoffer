#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   求1+2+---+n.py
@Time    :   2020/04/01 23:18:04
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case
             等关键字及条件判断语句（A?B:C）。
"""

# https://www.nowcoder.com/practice/7a0da8fc483247ff8800059e12d7caf1


class Solution:
    def __init__(self):
        self.res = 0

    def asum(self, n):
        self.res += n
        n -= 1
        return n > 0 and self.asum(n)

    def Sum_Solution(self, n):
        self.asum(n)
        return self.res


if __name__ == '__main__':
    print(Solution().Sum_Solution(100))
