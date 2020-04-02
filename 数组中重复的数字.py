#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   数组中重复的数字.py
@Time    :   2020/04/02 23:34:04
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   在一个长度为n的数组里的所有数字都在0到n-1的范围内。数组中某些数字是重复的，
             但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个
             重复的数字。例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出
             是第一个重复的数字2。
"""

# https://www.nowcoder.com/practice/623a5ac0ea5b4e5f95552655361ae0a8


class Solution:
    """
    从头到尾依次扫描这个数组中的每一个数字。在扫描到下标为i的数字时，首先比较这个数字
    （用m表示）是不是等于i。如果是，则接着扫描下一个数字；如果不是，则那它和第m个数字
    进行比较。如果他和第m个数字相等，就找到了一个重复数字（该数字在下标为i和m的位置都
    出现了）；如果它和第m个数字不相等，就把第i个数字和第m个数字交换，把m放到属于它的
    位置。接下来在重复这个比较、交换过程，直到我们发现一个重复的数字。
    """

    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if not numbers or len(numbers) == 1:
            return False

        for i in range(len(numbers)):
            m = numbers[i]
            while m != i:
                if m == numbers[m]:
                    duplication[0] = m
                    return True
                else:
                    numbers[i], numbers[m] = numbers[m], numbers[i]
                    m = numbers[i]
        return False


if __name__ == '__main__':
    print(Solution().duplicate([2, 3, 1, 0, 2, 5, 3], [-1]))
