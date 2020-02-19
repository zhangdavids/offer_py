# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n<1:  return 0
        if n==1: return 1
        last,ans,pos = 0,0,1
        while(n):
            num = n%10
            n = n/10
            ans += pos*n
            if num>1:
                ans+=pos
            elif num==1:
                ans+=(last+1)
            last = last+num*pos
            pos*=10
        return ans