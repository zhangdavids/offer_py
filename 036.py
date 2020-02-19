# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if numbers == []:
            return 0
        val,cnt = None,0
        for num in numbers:
            if cnt==0:
                val,cnt = num,1
            elif val == num:
                cnt+=1
            else:
                cnt-=1
        return val if numbers.count(val)*2>len(numbers) else 0