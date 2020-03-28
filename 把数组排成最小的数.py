#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   把数组排成最小的数.py
@Time    :   2020/03/28 23:34:31
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能
             拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打
             印出这三个数字能排成的最小数字为321323。
"""
from functools import cmp_to_key

# https://www.nowcoder.com/practice/8fecd3f8ba334add803bf2a06af1b993


class Solution:
    """
    两个数字m和n能拼接成数字mn和nm。如果mn<nm，那么应该打印mn，也就是m应该排在n
    的前面，我们定义此时m小于n；反之，如果nm<mn，则我们定义n小于m；如果mn=nm，则
    m等于n。
    """
    def _cmp(self, a, b):
        if a + b < b + a:
            return -1
        elif a + b > b + a:
            return 1
        else:
            return 0

    def PrintMinNumber(self, numbers):
        if not numbers:
            return ''
        nums = [str(num) for num in numbers]
        nums.sort(key=cmp_to_key(self._cmp))
        return ''.join(nums)


if __name__ == '__main__':
    print(Solution().PrintMinNumber([3, 32, 321]))
