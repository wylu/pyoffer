#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   矩阵中的路径.py
@Time    :   2020/04/07 22:46:38
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
             路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，
             向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入
             该格子。例如:
                [ a b c e
                  s f c s
                  a d e e ]
             矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串
             的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""

# https://www.nowcoder.com/practice/c61c6999eecb4b8f88a98f66b273a3cc


class Solution:
    """DFS"""
    ROWS = 0
    COLS = 0
    PATH = ''

    @staticmethod
    def search(matrix, x, y, visited, cur):
        cur += matrix[x][y]
        if cur == Solution.PATH:
            return True
        elif len(cur) >= len(Solution.PATH):
            return False
        elif cur != Solution.PATH[:len(cur)]:
            return False

        visited[x][y] = 1
        up, down = (x - 1, y), (x + 1, y)
        left, right = (x, y - 1), (x, y + 1)
        for dx, dy in (up, down, left, right):
            if (dx < 0 or dx >= Solution.ROWS or dy < 0 or dy >= Solution.COLS
                    or visited[dx][dy] == 1):
                continue
            if Solution.search(matrix, dx, dy, visited, cur):
                return True

        visited[x][y] = 0
        return False

    def hasPath(self, matrix, rows, cols, path):
        if not matrix or not rows or not cols or not path:
            return False
        Solution.ROWS, Solution.COLS = rows, cols
        Solution.PATH = path

        mat = [list(matrix[i * cols:i * cols + cols]) for i in range(rows)]

        flag = False
        visited = [[0] * cols for i in range(rows)]
        for x in range(rows):
            for y in range(cols):
                flag = Solution.search(mat, x, y, visited, '')
                if flag:
                    break
            if flag:
                break
        return flag


if __name__ == '__main__':
    # matrix = [
    #     ['a', 'b', 'c', 'e'],
    #     ['s', 'f', 'c', 's'],
    #     ['a', 'd', 'e', 'e'],
    # ]  # disable flake8

    matrix = 'abcesfcsadee'
    print(Solution().hasPath(matrix, 3, 4, 'bcced'))
    print(Solution().hasPath(matrix, 3, 4, 'abcb'))
