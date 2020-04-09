#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   剪绳子.py
@Time    :   2020/04/09 22:36:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），
             每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]可能的最大
             乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此
             时得到的最大乘积是18。输入一个数n，（2 <= n <= 60）
"""

# https://www.nowcoder.com/practice/57d85990ba5b440ab888fc72b0751bf8


class Solution:
    """
    贪心：
    当n>=5时，尽可能多地剪长度为3的绳子；当剩下的绳子长度为4时，把绳子剪成长度为2的绳子。
    """
    def cutRope(self, number):
        if number < 2:
            return 0
        if number == 2:
            return 1
        if number == 3:
            return 2

        # 尽可能多地剪去长度为3的绳子段
        times3 = number // 3
        # 当绳子最后剩下的长度为4时，不能再剪去长度为3的绳子段，因为2x2>3x1
        if number - times3 * 3 == 1:
            times3 -= 1
        times2 = (number - times3 * 3) // 2
        return pow(3, times3) * pow(2, times2)


if __name__ == '__main__':
    print(Solution().cutRope(8))
