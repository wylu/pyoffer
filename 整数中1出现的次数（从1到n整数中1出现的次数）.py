#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   整数中1出现的次数（从1到n整数中1出现的次数）.py
@Time    :   2020/03/28 22:40:04
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
             为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,
             但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,
             可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
"""

# https://www.nowcoder.com/practice/bd7f978302044eee894445e244c7eee6


class Solution:
    """找规律
    以 n=21345 为例：
    把 1~21345 的所有数字分为两段：一段是 1~1345；另一段是 1346~21345

    分析 1346~21345，1 的出现分两种情况：
    首先分析 1 出现在最高位的情况，在 1346~21345 的数字中，1 出现在 10000~19999
    这 10000 个数字的万位中，一个出现了 10000=10^4 次。也就是除去最高数字之后剩下
    的数字在加上 1（9999+1=10000）；
    然后分析 1 出现在除最高位之外的其它 4 位数中的情况，由于最高位是 2，可以再把
    1346~21345 分成两段：1346~11345 和 11346~21345。每一段剩下的4位数字中，选择
    其中一位是 1，其余三位可以在 0~9 这 10 个数字中任意选择，根据排列组合原则，总共
    出现的次数是 2x4x10^3=8000 次。

    至于在 1~1345 中 1 出现的次数，同理可以用递归求得，这也是为什么要把 1~21345
    分成 1~1345 和 1346~21345 两段的原因。

    因为把 21345 的最高位去掉就变成 1345，便于我们采用递归的思路。
    """
    @classmethod
    def num_of_1(cls, n):
        if not n:
            return 0

        first = int(n[0])
        if len(n) == 1 and first == 0:
            return 0
        if len(n) == 1 and first > 0:
            return 1

        # 假设 n=21345，则 num_first 是 10000~19999 的第一位中的1的数目
        num_first = 0
        if first > 1:
            num_first = pow(10, len(n) - 1)
        elif first == 1:
            num_first = int(n[1:]) + 1

        # num_other 是 1346~21345 除第一位之外的数位中的1的数目
        num_other = first * (len(n) - 1) * pow(10, len(n) - 2)
        # num_recur 是 1~1345 中的1的数目
        num_recur = Solution.num_of_1(n[1:])
        return num_first + num_other + num_recur

    def NumberOf1Between1AndN_Solution(self, n):
        if n < 1:
            return 0
        return Solution.num_of_1(str(n))


if __name__ == '__main__':
    print(Solution().NumberOf1Between1AndN_Solution(21345))
    print(Solution().NumberOf1Between1AndN_Solution(12345))
