#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   正则表达式匹配.py
@Time    :   2020/04/03 00:24:37
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'
             表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
             在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"
             与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
"""

# https://www.nowcoder.com/practice/45327ae22b7b413ea21df13ee7d6429c


class Solution:
    @classmethod
    def match_core(cls, s, sl, p, pl):
        if sl == len(s) and pl == len(p):
            return True
        if sl < len(s) and pl == len(p):
            return False

        if pl + 1 < len(p) and p[pl + 1] == '*':
            if sl == len(s):
                # s = ''
                return Solution.match_core(s, sl, p, pl + 2)
            elif p[pl] == s[sl] or (p[pl] == '.' and sl < len(s)):
                # move on the next state
                return (Solution.match_core(s, sl + 1, p, pl + 2)
                        # stay on the current state
                        or Solution.match_core(s, sl + 1, p, pl)
                        # ignore a*
                        or Solution.match_core(s, sl, p, pl + 2))
            else:
                # ignore a*
                return Solution.match_core(s, sl, p, pl + 2)

        if sl == len(s):
            # s = ''
            return False
        elif s[sl] == p[pl] or p[pl] == '.':
            return Solution.match_core(s, sl + 1, p, pl + 1)
        return False

    # s, pattern都是字符串
    def match(self, s, pattern):
        if s is None or pattern is None:
            return False
        return Solution.match_core(s, 0, pattern, 0)


if __name__ == '__main__':
    print(Solution().match('aaa', 'a.a'))
    print(Solution().match('aaa', 'ab*ac*a'))
    print(Solution().match('aa.a', 'ab*a'))
    print(Solution().match('', ''))
    print(Solution().match('ab', '.*'))
    print(Solution().match('aaa', 'a*a'))
    print(Solution().match('', '.*'))
    print(Solution().match('', '.'))
    print(Solution().match('', '.*a'))
