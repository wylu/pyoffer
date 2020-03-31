#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   翻转单词顺序.py
@Time    :   2020/03/31 23:52:17
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
             为简单起见，标点符合和普通字母一样处理。例如输入字符串
             "I am a student."，则输出"student. a am I"
"""

# https://www.nowcoder.com/practice/3194a4f4cf814f63919d0790578d51f3


class Solution:
    """
    第一步翻转句子中的所有字符。比如翻转"I am a student."中的所有字符得到
    ".tneduts a ma I"，此时不但翻转了句子中单词的顺序，连单词内的字符顺序
    也被翻转了。第二步在翻转每个单词中字符的顺序，就得到了"student. a am I"。
    """
    def reverse(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)

    def ReverseSentence(self, s):
        if not s or s.split() == []:
            return s
        s = self.reverse(list(s))
        print(len(s))
        print([self.reverse(list(item)) for item in s.split()])
        return ' '.join([self.reverse(list(item)) for item in s.split()])


if __name__ == '__main__':
    print(Solution().ReverseSentence('I am a student.'))
    print(len(Solution().ReverseSentence(' ')))
    print(len(Solution().ReverseSentence('   ')))
