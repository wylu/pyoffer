#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   字符串的排列.py
@Time    :   2020/03/27 22:47:28
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入一个字符串,按字典序打印出该字符串中字符的所有排列。
             例如输入字符串abc,则打印出由字符a,b,c所能排列出来的
             所有字符串abc,acb,bac,bca,cab和cba。
"""

# https://www.nowcoder.com/practice/fe6b651b66ae47d7acce78ffdd9a96c7


class Solution:
    """
    求整个字符串的排列，可以分为两步。
    第一步求出所有可能出现在第一个位置的字符，即把第一个字符和后面所有的字符交换。
    第二步固定第一个字符，求后面所有字符的排列。这时我们仍将后面的所有字符分成
    两部分：后面字符的第一个字符，以及这个字符之后的所有字符。然后把第一个字符
    逐一和它后面的字符交换。
    """
    @classmethod
    def permute(cls, seq, cur, res):
        if cur == len(seq) - 1:
            res.add(''.join(seq))
        else:
            for i in range(cur, len(seq)):
                seq[cur], seq[i] = seq[i], seq[cur]
                Solution.permute(seq, cur + 1, res)
                seq[cur], seq[i] = seq[i], seq[cur]

    def Permutation(self, ss):
        if not ss:
            return []
        res = set()
        Solution.permute(list(ss), 0, res)
        return sorted(res)


if __name__ == '__main__':
    print(Solution().Permutation('ab'))
    print(Solution().Permutation('abc'))
    print(Solution().Permutation('abac'))
