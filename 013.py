# -*- coding:utf-8 -*-

# 数字在排序数组中出现的次数
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        start = 0
        end = len(data) - 1
        while (start <= end):
            mid = (start + end) / 2
            if data[mid] == k:
                cnt = 0
                tmp = mid
                while (tmp >= 0 and data[tmp] == k):
                    cnt += 1
                    tmp -= 1
                tmp = mid + 1
                while (tmp < len(data) and data[tmp] == k):
                    cnt += 1
                    tmp += 1
                return cnt
            elif data[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
        return 0
