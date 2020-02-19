# -*- coding:utf-8 -*-

# 翻转单词顺序列


class Solution:
    def ReverseSentence(self, s):
        # write code here
        ret = s.split(" ")
        ret.reverse()
        return ' '.join(ret)


print(Solution().ReverseSentence("i love lily"))
