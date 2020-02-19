import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        heaps = []
        ret = []
        for num in tinput:
            heapq.heappush(heaps,num)
        if k>len(heaps):
            return []
        for i in range(k):
            ret.append(heapq.heappop(heaps))
        return ret