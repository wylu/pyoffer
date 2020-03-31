#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   和为S的两个数字.py
@Time    :   2020/03/31 23:19:51
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好
             是S，如果有多对数字的和等于S，输出两个数的乘积最小的。对应每个测试案例，
             输出两个数，小的先输出。
"""

# https://www.nowcoder.com/practice/390da4f7a00f44bea7c2f3d19491311b


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if not array or array[0] > tsum:
            return []

        left, right = 0, len(array) - 1
        min_res = pow(array[-1], 2)
        res = []
        while left < right:
            cur_sum = array[left] + array[right]
            if cur_sum == tsum:
                if array[left] * array[right] < min_res:
                    res = [array[left], array[right]]
                    min_res = array[left] * array[right]
                left += 1
            elif cur_sum > tsum:
                right -= 1
            else:
                left += 1
        return res


if __name__ == '__main__':
    # print(Solution().FindNumbersWithSum([1, 2, 4, 7, 11, 15], 15))
    print(Solution().FindNumbersWithSum([
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ], 21))
