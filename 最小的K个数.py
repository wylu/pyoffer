#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   最小的K个数.py
@Time    :   2020/03/28 21:44:46
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，
             则最小的4个数字是1,2,3,4。
"""

# https://www.nowcoder.com/practice/6a296eb82cf844ca8539b57c23e6e9bf


class Solution:
    """快速选择算法"""
    @classmethod
    def partition(cls, arr, left, right):
        j = left - 1
        # 选取最右元素为基准
        for i in range(left, right):
            if arr[i] <= arr[right]:
                j += 1
                arr[i], arr[j] = arr[j], arr[i]
        j += 1
        arr[right], arr[j] = arr[j], arr[right]
        return j

    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or k > len(tinput):
            return []

        left, right = 0, len(tinput) - 1
        while left <= right:
            idx = Solution.partition(tinput, left, right)
            if idx == k - 1:
                break
            if idx < k - 1:
                left = idx + 1
            else:
                right = idx - 1
        return sorted(tinput[:k])


if __name__ == '__main__':
    print(Solution().GetLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 3, 8], 4))
    print(Solution().GetLeastNumbers_Solution([4, 5, 1, 6, 2, 7, 3, 8], 8))
    print(Solution().GetLeastNumbers_Solution([2, 1], 2))
