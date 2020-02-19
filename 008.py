# -*- coding:utf-8 -*-

# 矩阵覆盖
class Solution:
    def rectCover(self, number):
        # write code here

        if number <= 2:
            return number
        dp = [1, 2]
        for i in range(number - 2):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]
