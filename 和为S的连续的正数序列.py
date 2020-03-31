#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   和为S的连续的正数序列.py
@Time    :   2020/03/31 22:56:38
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了
             正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为
             100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,
             20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? 
             Good Luck!
             输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字
             从小到大的顺序
"""

# https://www.nowcoder.com/practice/c451a3fd84b64cb19485dad758a55ebe


class Solution:
    """
    考虑用两个数small和big分别表示序列的最小值和最大值。首先把small初始化为1，
    big初始化为2。如果从small到big的序列的和大于s,则可以从序列中去掉较小的值，
    也就是增大small的值。如果从small到big的序列的和小于s,则可以增大big,让这个
    序列包含更多的数字。因为这个序列至少要有两个数字，所以我们一直增加small到
    (1+s)/2为止。
    """
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        res = []
        small, big, seq_sum = 1, 2, 3
        while small < (1 + tsum) // 2:
            if seq_sum == tsum and small < big:
                res.append([e for e in range(small, big + 1)])
                seq_sum -= small
                small += 1
            elif seq_sum > tsum:
                seq_sum -= small
                small += 1
            else:
                big += 1
                seq_sum += big
        return res


if __name__ == '__main__':
    print(Solution().FindContinuousSequence(15))
