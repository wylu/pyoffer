#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   替换空格.py
@Time    :   2020/03/17 11:20:34
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   请实现一个函数，将一个字符串中的每个空格替换成“%20”。
             例如，当字符串为We Are Happy.则经过替换之后的字符串
             为We%20Are%20Happy。
"""

# https://www.nowcoder.com/practice/4060ac7e3e404ad1a894ef3e17650423


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        return s.replace(' ', '%20')


if __name__ == '__main__':
    s = 'We Are Happy'
    print(Solution().replaceSpace(s))
