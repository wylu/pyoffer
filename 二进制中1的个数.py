#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   二进制中1的个数.py
@Time    :   2020/03/21 16:53:53
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""

# https://www.nowcoder.com/practice/8ee967e43c2c4ec193b040ea7fbb10b8
# 把一个整数减去1，再和原整数做与运算，会把该整数最右边的1变成0


class Solution:
    def NumberOf1(self, n):
        res = 0
        for _ in range(32):
            if n & 1 == 1:
                res += 1
            n >>= 1
        return res


if __name__ == '__main__':
    print(Solution().NumberOf1(-1))
    print(Solution().NumberOf1(5))
