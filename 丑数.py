#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   丑数.py
@Time    :   2020/03/29 16:16:20
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，
             但14不是，因为它包含质因子7。习惯上我们把1当做是第一个丑数。求按从小
             到大的顺序的第N个丑数。
"""

# https://www.nowcoder.com/practice/6aa9e04fc3794f68acf8778237ba065b


class Solution:
    """
    所谓一个数 m 是另一个数 n 的因子，是指 n 能被 m 整除，也就是 n % m == 0。
    根据丑数的定义，丑数只能被2、3和5整除。也就是说，如果一个数能被2整除，就连续
    除以2,；如果能被3整除，就连续除以3；如果能被5整除，就连续除以5。如果最后得到
    的是1，那么这个数就是丑数；否则不是。

    使用一个辅助数组保存找到的丑数，用空间换时间。

    根据丑数的定义，丑数应该是另一个丑数乘以2、3或者5的结果（1除外）。因此，我们
    可以创建一个数组，里面的数字是排好序的丑数，每个丑数都是前面的丑数乘以2、3或者
    5得到的。

    这种思路的关键在于如何确保数组中的丑数是排好序的。假设数组中已有若干个排好序的
    丑数，并且把已有的最大丑数记作 M，接下来分析如何生成下一个丑数。该丑数肯定是前
    面某一个丑数乘以2、3或者5的结果。

    首先考虑把已有的每个丑数都乘以2。在乘以2的时候，能得到若干个小于或等于 M 的结
    果，和若干个大于 M 的结果。由于是按照顺序生成的，小于或者等于 M 的肯定已经在
    数组中了，所以我们只需要第一个大于 M 的结果，并将其记为 Ｍ2。同理，把已有的丑
    数乘以３和５，能得到一个大于 M 的结果 M3 和 M5，那么下一个丑数就是 M2、M3
    和 M5 这3个数的最小者。

    进一步优化，对于乘以2而言，肯定存在某一个丑数 T2，排在它之前的丑数乘以2得到的
    结果都会小于已有的最大丑数，在它之后的每个丑数乘以2得到的结果都会太大。我们只需
    记下这个丑数的位置，同时每次生成新的丑数的时候去更新这个 T2 即可。对于乘以3和5
    而言，同样存在这样的 T3 和 T5。
    """
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0

        ugly, cnt = [1], 1
        t2, t3, t5 = 0, 0, 0

        while cnt < index:
            m = min(ugly[t2] * 2, ugly[t3] * 3, ugly[t5] * 5)
            ugly.append(m)

            while ugly[t2] * 2 <= m:
                t2 += 1
            while ugly[t3] * 3 <= m:
                t3 += 1
            while ugly[t5] * 5 <= m:
                t5 += 1

            cnt += 1

        return ugly[index - 1]


if __name__ == '__main__':
    print(Solution().GetUglyNumber_Solution(1500))
