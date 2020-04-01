#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   不用加减乘除做加法.py
@Time    :   2020/04/01 23:29:45
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
"""

# https://www.nowcoder.com/practice/59ac416b4b944300b617d4f7f111b215


class Solution:
    """
    以5+17=22为例，分三步：第一步只做各位相加不进位，此时相加的结果是12（个位数
    5和7相加不要进位是2，十位数0和1相加结果是1）；第二步做进位，5+7中有进位，进位
    的值是10；第三步把前面两个结果加起来，12+10的结果是22，刚好5+17=22。这种方法
    同样适用于二进制，在二进制中，加法可以用位运算替代。

    第一步不考虑进位对每一位相加，0+0,1+1的结果都是0；0+1,1+0的结果都是1,这和异或
    的结果是一样的。接着考虑第二步进位，对0+0,0+1,1+0,而言，都不会产生进位，只有
    1+1时，会向前产生一个进位，结果等同于两个数先做位与运算，然后再向左移动一位。第三
    步相加过程依然重复前面两步，直到不产生进位为止。

    ```python
    >>> print('{:b}'.format(-15 & 0xFFFFFFFF))
    11111111111111111111111111110001
    >>> print('{:032b}'.format((-15 & 0xFFFFFFFF) ^ 0xFFFFFFFF))
    00000000000000000000000000001110
    >>> print('{:032b}'.format(~((-15 & 0xFFFFFFFF) ^ 0xFFFFFFFF)))
    -0000000000000000000000000001111
    ```
    """
    def Add(self, num1, num2):
        while num2:
            sum = (num1 ^ num2) & 0xFFFFFFFF
            carry = ((num1 & num2) << 1) & 0xFFFFFFFF
            num1 = sum
            num2 = carry
        return num1 if num1 <= 0x7FFFFFFF else ~(num1 ^ 0xFFFFFFFF)


if __name__ == '__main__':
    print(Solution().Add(5, 17))
    print(Solution().Add(5, -1))
    print(Solution().Add(-6, -1))
