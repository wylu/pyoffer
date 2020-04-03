#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   字符流中第一个不重复的字符.py
@Time    :   2020/04/04 00:26:54
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流
             中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中
             读出前六个字符“google"时，第一个只出现一次的字符是"l"。如果当前字符
             流没有存在出现一次的字符，返回#字符。
"""

# https://www.nowcoder.com/practice/00de97733b8e4f97a3fb5c680ee10720


class Solution:
    def __init__(self):
        self.idx = [-1 for _ in range(256)]
        self.cur = 0

    # 返回对应char
    def FirstAppearingOnce(self):
        min_idx = 0x7FFFFFFF
        ch = '#'
        for i, e in enumerate(self.idx):
            if e >= 0 and e < min_idx:
                min_idx = e
                ch = chr(i)
        return ch

    def Insert(self, char):
        if self.idx[ord(char)] == -1:
            self.idx[ord(char)] = self.cur
        elif self.idx[ord(char)] >= 0:
            self.idx[ord(char)] = -2
        self.cur += 1


if __name__ == '__main__':
    s = Solution()
    print(s.FirstAppearingOnce())
    for ch in 'google':
        s.Insert(ch)
        print(s.FirstAppearingOnce())
