#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   数值的整数次方.py
@Time    :   2020/03/21 21:24:57
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   给定一个double类型的浮点数base和int类型的整数exponent。
             求base的exponent次方。保证base和exponent不同时为0
"""

# https://www.nowcoder.com/practice/1a834e5e3e1a4b7ba251417554e07c00


class Solution:
    """
    快速幂
    2^5=2^(101)=2^(4)*2^(0)*2^(1)=2^(100)*2^(000)*2^(001)=32
    """
    def Power(self, base, exponent):
        exp = abs(exponent)
        res = 1
        while exp != 0:
            if exp & 1 == 1:
                res *= base
            base *= base
            exp >>= 1
        return res if exponent >= 0 else 1 / res


if __name__ == '__main__':
    print(Solution().Power(2, 5))
    print(Solution().Power(3, 5))
    print(Solution().Power(2, -3))
