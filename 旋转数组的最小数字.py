#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   旋转数组的最小数字.py
@Time    :   2020/03/19 23:05:09
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
             输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。例如
             数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
             给出的所有元素都大于0，若数组大小为0，请返回0。
"""

# https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba


class Solution:
    """
    二分查找，用两个指针分别指向数组的第一个元素和最后一个元素。
    """
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        left, right = 0, len(rotateArray) - 1
        if rotateArray[left] == rotateArray[right]:
            return min(rotateArray)

        while right - left > 1:
            mid = (left + right) // 2
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            else:
                right = mid
        return min(rotateArray[left], rotateArray[right])


if __name__ == '__main__':
    print(Solution().minNumberInRotateArray([3, 4, 5, 1, 2]))
    print(Solution().minNumberInRotateArray([1, 0, 1, 1, 1]))
    print(Solution().minNumberInRotateArray([3, 4, 5, 6, 1, 2]))
