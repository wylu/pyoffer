#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   构建乘积数组.py
@Time    :   2020/04/02 23:58:06
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的
             元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
             （注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = 
             A[0] * A[1] * ... * A[n-2];）
"""

# https://www.nowcoder.com/practice/94a4d381a68b47b7a8bed86f2975db46


class Solution:
    """
      B[0]:  1    A[1]  A[2]   ...    A[n-2]  A[n-1]
      B[1]: A[0]   1    A[2]   ...    A[n-2]  A[n-1]
      B[2]: A[0]  A[1]   1     ...    A[n-2]  A[n-1]
      ...   A[0]  A[1]  ...     1     A[n-2]  A[n-1]
    B[n-2]: A[0]  A[1]  ...   A[n-3]    1     A[n-1]
    B[n-1]: A[0]  A[1]  ...   A[n-3]  A[n-2]    1

    定义C[i]=A[0]xA[1]x...xA[i-1], D[i]=A[i+1]x...xA[n-2]xA[n-1]。
    C[i]=C[i-1]xA[i-1], D[i]=D[i+1]xA[i+1]
    """
    def multiply(self, A):
        if not A:
            return []

        B = [1] * len(A)
        for i in range(1, len(A)):
            B[i] = B[i - 1] * A[i - 1]

        tmp = 1
        for i in range(len(A) - 2, -1, -1):
            tmp *= A[i + 1]
            B[i] *= tmp
        return B


if __name__ == '__main__':
    print(Solution().multiply([1, 2, 3, 4, 5]))
