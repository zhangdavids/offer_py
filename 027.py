# 滑动窗口的最大值
#
# 给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
# 思考：假设当前窗口起始位置为start,结束位置为end，我们要构造一个stack, 使得stack[0]为区间[start,end]的最大值。


# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size == 0:
            return []
        ret = []
        stack = []
        for pos in range(len(num)):
            while (stack and stack[-1][0] < num[pos]):
                stack.pop()
            stack.append((num[pos], pos))
            if pos >= size - 1:
                while (stack and stack[0][1] <= pos - size):
                    stack.pop(0)
                ret.append(stack[0][0])
        return ret