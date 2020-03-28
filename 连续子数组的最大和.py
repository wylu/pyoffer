#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   连续子数组的最大和.py
@Time    :   2020/03/28 22:23:09
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,
             他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量
             全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个
             负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续
             子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大
             连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
"""

# https://www.nowcoder.com/practice/459bd355da1549fa8a49e350bf3df484


class Solution:
    """Dynamic Programming

    State:
      dp[i]: 表示以a[i]为结尾的连续子向量的最大和

    Initial State:
      dp[i] = 0

    State Transition:
      if dp[i - 1] <= 0:
          dp[i] = a[i]
      else:
          dp[i] = dp[i - 1] + a[i]
    """
    def FindGreatestSumOfSubArray(self, array):
        res, dp = array[0], 0
        for e in array:
            dp = e if dp <= 0 else dp + e
            res = max(res, dp)
        return res


if __name__ == '__main__':
    print(Solution().FindGreatestSumOfSubArray([6, -3, -2, 7, -15, 1, 2, 2]))
