# -*- coding:utf-8 -*-

# 跳台阶
class Solution:
    def jumpFloor(self, number):
        # write code here
        """
        n = 1 : 1
        n = 2 : 1+1 = 2
        n = 3 : dp[n-2]+dp[n-1]
        """
        if number == 1 or number == 2:
            return number
        dp = [1, 2]
        for _ in range(number - 2):
            dp.append(dp[-1] + dp[-2])
        return dp[-1]
