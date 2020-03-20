#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   矩形覆盖.py
@Time    :   2020/03/20 23:05:46
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1
             的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""

# https://www.nowcoder.com/practice/72a5a919508a4251859fb2cfb987a0e6


class Solution:
    @classmethod
    def cover(cls, n):
        res = [0, 1, 2]
        if n <= 2:
            return res[n]
        else:
            for _ in range(3, n + 1):
                res[1], res[2] = res[2], res[1] + res[2]
            return res[2]

    def rectCover(self, number):
        return Solution.cover(number)


if __name__ == '__main__':
    print(Solution().rectCover(3))
