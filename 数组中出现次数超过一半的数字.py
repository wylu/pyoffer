#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   数组中出现次数超过一半的数字.py
@Time    :   2020/03/27 23:26:54
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
             例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数
             组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""

# https://www.nowcoder.com/practice/e8a1b01a2df14cb2b228b30ee6a92163


class Solution:
    """
    解法一：快速选择算法查找数组中位数。

    解法二：在遍历数组时保存两个值：一个是数组的一个数字；另一个是次数。
    当遍历到下一个数字时，如果下一个数字和之前保存的数字相同，则次数加1；
    如果下一个数字和之前保存的数字不同，则次数减一。如果次数为0，那么需要
    保存下一个数字，并将次数设为1。（由于我们要找的数字出现的次数比其他所
    有数字出现的次数之和还要多，那么要找的数字肯定是最后一次把次数设为1时
    的数字）
    """
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0

        cnt = 0
        for num in numbers:
            if cnt == 0:
                mid, cnt = num, 1
            else:
                cnt += 1 if num == mid else -1

        valid = sum(1 for num in numbers if num == mid) > len(numbers) / 2
        return mid if valid else 0


if __name__ == '__main__':
    print(Solution().MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))
    print(Solution().MoreThanHalfNum_Solution([1, 2, 3, 2, 4, 2, 5, 2, 3]))
