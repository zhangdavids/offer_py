import bisect
class Solution:
    def InversePairs(self, data):
        data.reverse()
        L = []
        ret = 0
        for d in data:
            pos = bisect.bisect_left(L,d)
            L.insert(pos,d)
            ret+= pos
            ret = ret % 1000000007
        return ret % 1000000007