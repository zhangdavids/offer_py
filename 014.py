# 数组中只出现一次的数字

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        ans, a1, a2, flag = 0, 0, 0, 1
        for num in array:
            ans = ans ^ num
        while (ans):
            if ans % 2 == 0:
                ans = ans >> 1
                flag = flag << 1
            else:
                break
        for num in array:
            if num & flag:
                a1 = a1 ^ num
            else:
                a2 = a2 ^ num
        return a1, a2
