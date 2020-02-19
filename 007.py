# 变态跳台阶

class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1 or number == 2:
            return number
        ret = sum_ = 3
        for i in range(number - 2):
            ret = sum_ + 1
            sum_ += ret
        return ret
