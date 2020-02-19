class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array)==1:
            return array[0]
        cur = pos = array[0]
        for i in range(1,len(array)):
            pos = max(pos+array[i],array[i])
            cur = max(cur,pos)
        return cur