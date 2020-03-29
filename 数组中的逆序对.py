#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   数组中的逆序对.py
@Time    :   2020/03/29 22:26:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字
             组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将
             P对1000000007取模的结果输出。即输出P%1000000007
"""

# https://www.nowcoder.com/practice/96bd6684e04a44eb80e6a68efc0ec6c5


class Solution:

    MOD = 1000000007

    """
    基于归并排序的逆序对统计：
    先把数组分隔成子数组，统计出子数组内部的逆序对的数目，然后在统计出两个相邻
    子数组之间的逆序对的数目。在统计逆序对的过程中，还需要对数组进行排序。实际
    上这个过程就是归并排序的过程。
    """
    @classmethod
    def merge(cls, arr, left, mid, right):
        pass

    @classmethod
    def recursive(cls, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            cnt_left = Solution.recursive(arr, left, mid)
            cnt_right = Solution.recursive(arr, mid + 1, right)
            cnt = Solution.merge(arr, left, mid, right)
            return (cnt_left + cnt_right + cnt) % Solution.MOD
        return 0

    def InversePairs(self, data):
        if not data:
            return 0
        return Solution.recursive(data, 0, len(data) - 1)


if __name__ == '__main__':
    print(Solution().InversePairs([7, 5, 6, 4]))
