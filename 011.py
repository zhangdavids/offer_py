# 和为S的连续正数序列

class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        k = 2
        ret = []
        for k in range(2,tsum):
            if k%2==1 and tsum%k==0:
                tmp = []
                mid = tsum/k
                if mid-k/2>0:
                    for i in range(mid-k/2,mid+k/2+1):
                        tmp.append(i)
                    ret.append(tmp[:])
            elif k%2==0 and (tsum%k)*2==k:
                mid = tsum/k
                tmp = []
                if mid-k/2+1>0:
                    for i in range(mid-k/2+1,mid+k/2+1):
                        tmp.append(i)
                    ret.append(tmp[:])
        ret.sort()
        return ret