# -*- coding:utf-8 -*-

# 左旋转字符串
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if s == '':
            return s
        n = n % len(s)
        return s[n:] + s[0:n]
