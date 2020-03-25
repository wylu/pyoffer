#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   栈的压入弹出序列.py
@Time    :   2020/03/25 23:16:07
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为
             该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈
             的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2
             就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
"""

# https://www.nowcoder.com/practice/d77d11405cc7470d82554cb392585106


class Solution:
    """
    模拟入栈、出栈过程。
    如果入栈的数字刚好是出栈栈顶数字，那么直接弹出；如果入栈数字不是出栈栈顶数字，
    那么将该数字压入辅助栈中。待入栈数字耗尽时，判断辅助栈的数字能否按照出栈的剩余
    数字顺序弹出。
    """
    def IsPopOrder(self, pushV, popV):
        if not pushV or not popV or len(pushV) != len(popV):
            return False

        stack = []
        for e in pushV:
            if e == popV[0]:
                popV = popV[1:]
            else:
                stack.append(e)

        if len(stack) != len(popV):
            return False

        while stack:
            if stack.pop() != popV[0]:
                return False
            else:
                popV = popV[1:]
        return True


if __name__ == '__main__':
    print(Solution().IsPopOrder([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    print(Solution().IsPopOrder([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
