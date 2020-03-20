#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   变态跳台阶.py
@Time    :   2020/03/20 22:35:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
             求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""

# https://www.nowcoder.com/practice/22243d016f6b47f2a6928b4313c85387


class Solution:
    """
    f(n)=2^(n-1)
    """
    def jumpFloorII(self, n):
        if n <= 0:
            return 0
        return 2**(n - 1)


if __name__ == '__main__':
    print(Solution().jumpFloorII(5))
