#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   跳台阶.py
@Time    :   2020/03/20 22:24:25
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级
             的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""

# https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4


class Solution:

    # @classmethod
    # def jump(cls, n):
    #     if n <= 2:
    #         return n
    #     else:
    #         return Solution.jump(n - 1) + Solution(n - 2)

    @classmethod
    def jump(cls, n):
        if n <= 2:
            return n
        else:
            a, b = 1, 2
            for i in range(3, n + 1):
                a, b = b, a + b
            return b

    def jumpFloor(self, number):
        if number <= 0:
            return 0
        return Solution.jump(number)


if __name__ == '__main__':
    print(Solution().jumpFloor(5))
