# -*- coding:utf-8 -*-
import heapq


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return 0
        heaps = []
        heapq.heappush(heaps, 1)
        lastnum = None
        idx = 1
        while (idx <= index):
            curnum = heapq.heappop(heaps)
            while (curnum == lastnum):
                curnum = heapq.heappop(heaps)
            lastnum = curnum
            idx += 1
            heapq.heappush(heaps, curnum * 2)
            heapq.heappush(heaps, curnum * 3)
            heapq.heappush(heaps, curnum * 5)
        return lastnum


print(Solution().GetUglyNumber_Solution(20))
