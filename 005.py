# -*- coding:utf-8 -*-

# 斐波那契数列
class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        memories = [1, 1]
        for _ in range(n - 2):
            memories.append(memories[-1] + memories[-2])
        return memories[-1]
