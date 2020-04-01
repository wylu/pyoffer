#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   圆圈中最后剩下的数字.py
@Time    :   2020/04/01 22:57:25
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   0,1,...,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除
             第m个数字。求出这个圆圈里剩下的最后一个数字。
"""

# https://www.nowcoder.com/practice/f78a359491e64a50bce2d89cff857eb6


class Solution:
    """
    约瑟夫环
    定义一个关于n和m的方程f(n,m)，表示每次在n个数字0,1,...,n-1中删除第m个数字最后
    剩下的数字。
    f(n,m)=0, n=1
    f(n,m)=[f(n-1,m)+m]%n, n>1
    """
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1

        last = 0
        for i in range(2, n + 1):
            last = (last + m) % i
        return last


if __name__ == '__main__':
    print(Solution().LastRemaining_Solution(5, 3))
