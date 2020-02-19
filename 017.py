# -*- coding:utf-8 -*-

# 和为S的两个数字

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        memorys = {}
        ret = []
        for num in array:
            if tsum - num in memorys:
                if ret is []:
                    ret = [tsum - num, num]
                elif ret and ret[0] * ret[1] > (tsum - num) * num:
                    ret = [tsum - num, num]
            else:
                memorys[num] = 1
        return ret
