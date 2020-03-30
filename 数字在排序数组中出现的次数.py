#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   数字在排序数组中出现的次数.py
@Time    :   2020/03/30 22:03:03
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   统计一个数字在排序数组中出现的次数。
"""

# https://www.nowcoder.com/practice/70610bf967994b22bb1c26f9ae901fa2


class Solution:
    """
    利用二分查找在数组中分别找到第一个k和最后一个k，即可统计出k出现的次数。
    """
    def get_first_k(self, arr, k):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > k:
                right = mid - 1
            elif arr[mid] < k:
                left = mid + 1
            else:
                if mid - 1 < left or arr[mid - 1] < k:
                    return mid
                else:
                    right = mid - 1
        return -1

    def get_last_k(self, arr, k):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > k:
                right = mid - 1
            elif arr[mid] < k:
                left = mid + 1
            else:
                if mid + 1 > right or arr[mid + 1] > k:
                    return mid
                else:
                    left = mid + 1
        return -1

    def GetNumberOfK(self, data, k):
        if not data:
            return 0

        first_k = self.get_first_k(data, k)
        last_k = self.get_last_k(data, k)
        return 0 if first_k == -1 else last_k - first_k + 1


if __name__ == '__main__':
    print(Solution().GetNumberOfK([1, 2, 3, 3, 3, 3, 4, 5], 3))
    print(Solution().GetNumberOfK([1, 3, 3, 3, 3, 4, 5], 2))
