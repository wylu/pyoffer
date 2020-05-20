#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   顺时针打印矩阵.py
@Time    :   2020/03/24 22:28:51
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
             例如，如果输入如下 4X4 矩阵：
                 1  2  3  4
                 5  6  7  8
                 9  10 11 12
                 13 14 15 16
             则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10
"""

# https://www.nowcoder.com/practice/9b4c81a02cd34f76be2659fa0d54342a


class Solution:
    """
    用一个循环来打印矩阵，每次打印矩阵中的一个圈。

    分析循环结束的条件：
    假设这个矩阵的行数是 rows，列数是 cols，打印第一圈的左上角的坐标为(0,0)，
    第二圈的左上角的坐标是(1,1)，以此类推。

    可以发现，左上角的坐标中行标和列标总是相同的，于是在矩阵中选取左上角为
    (start,start)的一圈作为分析的目标。

    对于一个 5x5 的矩阵而言，最后一圈只有一个数字，对应的坐标为(2,2)。可以发现
    5>2x2。对于一个 6x6 的矩阵而言，最后一圈有4个数字，其左上角的坐标任然为
    (2,2)。可以发现 6>2x2 依然成立。

    于是可以得出，让循环继续的条件是 cols > startX*2 并且 rows > startY*2

    循环打印时，需要注意一些比较特殊的矩阵，如： 2x3，3x1，1x2
    """
    @classmethod
    def prt_circle(cls, matrix, rows, cols, start, res):
        end_x = cols - start
        end_y = rows - start

        # 从左到右打印一行
        for i in range(start, end_x):
            res.append(matrix[start][i])

        if start < end_y - 1:
            # 从上到下打印一列
            for i in range(start + 1, end_y):
                res.append(matrix[i][end_x - 1])

            if start < end_x - 1:
                # 从右到左打印一行
                for i in range(end_x - 2, start - 1, -1):
                    res.append(matrix[end_y - 1][i])

                if start < end_y - 2:
                    # 从下到上打印一列
                    for i in range(end_y - 2, start, -1):
                        res.append(matrix[i][start])

    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if not matrix:
            return []

        res = []
        rows, cols = len(matrix), len(matrix[0])
        start = 0
        while cols > start * 2 and rows > start * 2:
            Solution.prt_circle(matrix, rows, cols, start, res)
            start += 1
        return res


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(Solution().printMatrix(matrix))
