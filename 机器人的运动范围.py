#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   机器人的运动范围.py
@Time    :   2020/04/08 22:21:14
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次
             只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数
             位之和大于k的格子。例如，当k为18时，机器人能够进入方格（35,37），
             因为3+5+3+7=18。但是，它不能进入方格（35,38），因为3+5+3+8=19。
             请问该机器人能够达到多少个格子？
"""

# https://www.nowcoder.com/practice/6e5207314b5241fb83f2329e89fdecc8


class Solution:
    ROWS = 0
    COLS = 0
    THRESHOLD = 0

    @staticmethod
    def nbsum(x):
        res = 0
        while x:
            res += x % 10
            x //= 10
        return res

    @staticmethod
    def check(x, y, visited):
        if (x < 0 or x >= Solution.ROWS or y < 0 or y >= Solution.COLS
                or visited[x][y]):
            return False
        return Solution.nbsum(x) + Solution.nbsum(y) <= Solution.THRESHOLD

    @staticmethod
    def search(x, y, visited):
        cnt = 0
        if Solution.check(x, y, visited):
            visited[x][y] = True
            up = Solution.search(x - 1, y, visited)
            down = Solution.search(x + 1, y, visited)
            left = Solution.search(x, y - 1, visited)
            right = Solution.search(x, y + 1, visited)
            cnt = 1 + up + down + left + right
        return cnt

    def movingCount(self, threshold, rows, cols):
        if rows <= 0 or cols <= 0 or threshold < 0:
            return 0
        Solution.ROWS, Solution.COLS = rows, cols
        Solution.THRESHOLD = threshold

        visited = [[False] * cols for _ in range(rows)]
        return Solution.search(0, 0, visited)


if __name__ == '__main__':
    print(Solution().movingCount(1, 2, 2))
