#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   把字符串转换成整数.py
@Time    :   2020/04/02 22:52:19
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。
             数值为0或者字符串不是一个合法的数值则返回0
             输入描述：输入一个字符串,包括数字字母符号,可以为空
             输出描述：如果是合法的数值表达则返回该数字，否则返回0
             +2147483647 -> 2147483647
             1a33 -> 0
"""

# https://www.nowcoder.com/practice/1277c681251b4372bdef344468e4f26e


class Solution:
    def StrToInt(self, s):
        if not s:
            return 0

        sign = -1 if s[0] == '-' else 1
        if s[0] == '-' or s[0] == '+':
            s = s[1:]

        res = 0
        for ch in s:
            if ord(ch) < ord('0') or ord(ch) > ord('9'):
                return 0
            # res = res * 10 + ord(ch) - ord('0')
            res = (res << 1) + (res << 3) + (ord(ch) & 0xF)
        res *= sign
        if res > 0x7FFFFFFF or res < -0x80000000:
            return 0
        else:
            return res


if __name__ == '__main__':
    print(Solution().StrToInt('+1a33'))
    print(Solution().StrToInt('+2147483647'))
    print(Solution().StrToInt('+2147483648'))
    print(Solution().StrToInt('-2147483648'))
    print(Solution().StrToInt('-2147483649'))
