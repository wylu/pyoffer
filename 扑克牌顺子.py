#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   扑克牌顺子.py
@Time    :   2020/04/01 22:37:30
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
             2~10为数字本身，A为1，J为11，Q为12，K为13，而大、小王可以看成
             任何数字，输入中把它定义为0。
"""

# https://www.nowcoder.com/practice/762836f4d43d43ca9deb273b3de8e1f4


class Solution:
    """
    首先把数组排序；其次统计数组中的0的个数；最后统计排序后数组中相邻数字之间的空缺数。
    如果空缺的总数小于等于0的个数，那么这个数组就是连续的；反之则不连续。需要注意的是，
    如果数组中的非0数字重复出现，则该数组不是连续的。
    """
    def IsContinuous(self, numbers):
        if not numbers or len(numbers) != 5:
            return False

        zero_cnt = 0
        for num in numbers:
            if num == 0:
                zero_cnt += 1

        numbers.sort()

        p1, p2 = zero_cnt, zero_cnt + 1 
        gap_cnt = 0
        while p2 < len(numbers):
            if numbers[p1] == numbers[p2]:
                return False
            gap_cnt += numbers[p2] - numbers[p1] - 1
            p1 += 1
            p2 += 1
        return True if gap_cnt <= zero_cnt else False


if __name__ == '__main__':
    print(Solution().IsContinuous([0, 1, 3, 4, 5]))
