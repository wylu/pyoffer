#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   左旋转字符串.py
@Time    :   2020/03/31 23:42:52
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，
             就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，请你
             把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求
             输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
"""

# https://www.nowcoder.com/practice/12d959b108cb42b1ab72cef4d36af5ec


class Solution:
    """
    以s="abcdefg",n=2为例，我们可以它分成两部分。把前两个字符分到第一部分，
    把后面的所有字符分到第二部分。然后分别翻转这个两部分，于是就得到了"bagfedc"。
    最后翻转整个字符串，得到的"cdefgab"刚好就是把原字符串左旋两位的结果。
    """
    def LeftRotateString(self, s, n):
        return s[n:] + s[:n] if s else ''


if __name__ == '__main__':
    print(Solution().LeftRotateString('abcdefg', 2))
