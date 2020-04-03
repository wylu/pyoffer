#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   表示数值的字符串.py
@Time    :   2020/04/03 23:32:04
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，
             字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
             但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""

# https://www.nowcoder.com/practice/6f8c901d091949a5837e24bb82a731f2


class Solution:
    """
    数字的格式可以用 A[.[B]][e|EC] 或 .B[e|EC] 表示，其中 A 和 C 都是整数
    （可以有正负号，也可以没有）， 而 B 是一个无符号整数
    """
    def scan_unsigned_int(self, s, cur):
        start = cur[0]
        while cur[0] < len(s) and '0' <= s[cur[0]] <= '9':
            cur[0] += 1
        return cur[0] > start

    def scan_int(self, s, cur):
        if cur[0] < len(s) and (s[cur[0]] == '+' or s[cur[0]] == '-'):
            cur[0] += 1
        return self.scan_unsigned_int(s, cur)

    # s字符串
    def isNumeric(self, s):
        if not s:
            return False

        cur = [0]
        numeric = self.scan_int(s, cur)
        if cur[0] < len(s) and s[cur[0]] == '.':
            cur[0] += 1
            # 用or的原因：
            # 1.小数可以没有整数，如 .123 = 0.123
            # 2.小数点后面可以没有数字，如 233. = 233.0
            # 3.前面和后面可以都有数字， 如 233.666
            numeric = self.scan_unsigned_int(s, cur) or numeric
        if cur[0] < len(s) and (s[cur[0]] == 'e' or s[cur[0]] == 'E'):
            cur[0] += 1
            # 用and的原因：
            # 1.当e或E前面没有数字时，整个字符串不能表示数字，如 .e1 , e1
            # 2.当e或E后面没有整数时，整个字符串不能表示数字，如 12e , 12e+5.4
            numeric = numeric and self.scan_int(s, cur)
        return numeric and cur[0] == len(s)


if __name__ == '__main__':
    # print(Solution().isNumeric('-1E-16'))
    # print(Solution().isNumeric('1a3.14'))
    # print(Solution().isNumeric('12e+4.3'))
    # print(Solution().isNumeric('+-5'))
    # print(Solution().isNumeric('12e'))
    # print(Solution().isNumeric('100'))
    print(Solution().isNumeric('123.45e+6'))
