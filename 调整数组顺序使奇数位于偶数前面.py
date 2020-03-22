#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   调整数组顺序使奇数位于偶数前面.py
@Time    :   2020/03/22 18:17:22
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得
             所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
             并保证奇数和奇数，偶数和偶数之间的相对位置不变。

             剑指Offer原题并不需要保证相对位置不变，所以在这种请情况下，
             可以维护两个指针：第一个指针初始化时指向数组的第一个数字，它
             只向后移动；第二个指针初始化时指向数组的最后一个数字，它只向
             前移动。在两个指针相遇之前，第一个指针总是位于第二个指针的前
             面。如果第一个指针指向的数字是偶数，并且第二个指针指向的数字
             是技术，则交换这两个数字。
"""

# https://www.nowcoder.com/practice/beb5aa231adc45b2a5dcc5b62c93f593


class Solution:
    def reOrderArray(self, array):
        return [e for e in array if e & 1 == 1
                ] + [e for e in array if e & 1 == 0]


if __name__ == '__main__':
    print(Solution().reOrderArray([1, 2, 3, 4, 5]))
    print(Solution().reOrderArray([1, 2, 3, 4, 5, 6]))
