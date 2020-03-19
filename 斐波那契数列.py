#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   斐波那契数列.py
@Time    :   2020/03/19 23:50:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列
             的第n项（从0开始，第0项为0）。n<=39
"""

# https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3


class Solution:

    # @classmethod
    # def fibo(cls, n):
    #     if n == 0:
    #         return 0
    #     elif n == 1 or n == 2:
    #         return 1
    #     else:
    #         return Solution.fibo(n - 1) + Solution.fibo(n - 2)

    @classmethod
    def fibo(cls, n):
        res = [0, 1, 1]
        if n <= 2:
            return res[n]
        else:
            for i in range(3, n + 1):
                res[1], res[2] = res[2], res[1] + res[2]
            return res[2]

    def Fibonacci(self, n):
        return Solution.fibo(n)


if __name__ == '__main__':
    print(Solution().Fibonacci(0))
    print(Solution().Fibonacci(8))
