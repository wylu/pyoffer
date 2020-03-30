#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   数组中只出现一次的数字.py
@Time    :   2020/03/30 22:50:40
@Author  :   wylu
@Version :   1.0
@Contact :   15wylu@gmail.com
@License :   (C)Copyright 2020, wylu-CHINA-SHENZHEN
@Desc    :   一个整型数组里除了两个数字之外，其他的数字都出现了两次。
             请写程序找出这两个只出现一次的数字。
"""

# https://www.nowcoder.com/practice/e02fdb54d7524710a7d664d082bb7811


class Solution:
    """
    考虑数组中只有一个数子只出现了一次，其它数字都出现了两次，怎么找出这个数字？
    异或运算的一个性质：任何一个数字异或它本身都等于0。也就是说，如果从头到尾异或
    数组中的每一个数字，那么最终结果刚好是那个只出现一次的数字。

    如果能够把原数组分成两个子数组，每个子数组都只包含一个出现一次的数字，那么就可
    以使用上面的结论。

    拆分数组：
    从头到尾异或数组中的每一个数字，由于这个两个出现一次的数字不一样，所以异或的结
    果肯定不为0，也即，在这个结果数字的二进制表示中至少有一位为1。我们在结果数字中
    找到第一个为1的位的位置，记为第n位。接着以第n位是不是1为标准将原数组划分为两个
    子数组。由于分组的标准是数字中的某一位是否是1，那么出现了两次的数字一定会被分配
    到同一个组，而两个只出现一次的数字将会分配到不同的组。
    """

    # 返回[a,b] 其中a,b是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        xor = 0
        for num in array:
            xor ^= num

        n = 0
        while xor & 1 != 1 and n < 32:
            xor >>= 1
            n += 1

        if n == 32:
            return

        res = [0, 0]
        for num in array:
            if num >> n & 1 == 1:
                res[0] ^= num
            else:
                res[1] ^= num
        return res


if __name__ == '__main__':
    print(Solution().FindNumsAppearOnce([2, 4, 3, 6, 3, 2, 5, 5]))
