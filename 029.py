# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray == []:
            return 0
        _len = len(rotateArray)
        left = 0
        right = _len - 1
        while left <= right:
            mid = int((left + right) >> 1)
            if rotateArray[mid] < rotateArray[mid - 1]:
                return rotateArray[mid]
            if rotateArray[mid] >= rotateArray[right]:
                # 说明在【mid，right】之间
                left = mid + 1
            else:
                # 说明在【left，mid】之间
                right = mid - 1
        return rotateArray[mid]
