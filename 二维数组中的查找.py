#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   二维数组中的查找.py
@Time    :   2020/03/15 22:58:55
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   在一个二维数组中（每个一维数组的长度相同），每一行都按照
             从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
             请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中
             是否含有该整数。
"""

# https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e

# 当我们需要解决一个复杂的问题时，一个行之有效的方法就是从一个具体的问题
# 入手，通过分析简单具体的例子，视图寻找普遍的规律。


class Solution:
    """
    首先选取数组中右上角的数字。如果该数字等于要查找的数字，则查找结束；
    如果该数字大于要查找的数字，则剔除这个数字所在的列；如果该数字小于要
    查找的数字，则剔除这个数字所在的行。重复以上步骤，直到找到要查找的数
    字，或者查找范围为空。
    """

    # array 二维列表
    def Find(self, target, array):
        row, col = 0, len(array[0]) - 1
        while row < len(array) and col >= 0:
            if array[row][col] == target:
                return True
            elif array[row][col] > target:
                col -= 1
            else:
                row += 1
        return False


if __name__ == '__main__':
    array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    target = 7
    print(Solution().Find(target, array))
