#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   第一个只出现一次的字符.py
@Time    :   2020/03/29 22:06:29
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只
             出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）
"""

# https://www.nowcoder.com/practice/1c82e8cf713b4bbeb2a5b31cf5b0417c


class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1

        counter = {}
        for ch in s:
            counter[ch] = counter.get(ch, 0) + 1

        res = ''
        for ch, cnt in counter.items():
            if cnt == 1:
                res = ch
                break

        if not res:
            return -1
        else:
            for i, ch in enumerate(s):
                if counter[ch] == 1:
                    return i


if __name__ == '__main__':
    print(Solution().FirstNotRepeatingChar('abaccdeff'))
    print(Solution().FirstNotRepeatingChar('google'))
