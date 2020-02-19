# -*- coding:utf-8 -*-

# 顺时针打印矩阵
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        m = len(matrix)
        ans = []
        if m == 0:
            return ans
        n = len(matrix[0])
        # ans = [[0 for i in range(n)] for j in range(n)]
        # print ans
        upper_i = 0
        lower_i = m - 1
        left_j = 0
        right_j = n - 1
        num = 1
        i = 0
        j = 0
        right_pointer = 1
        down_pointer = 0
        while (num <= m * n):
            ans.append(matrix[i][j])
            if right_pointer == 1:
                if j < right_j:
                    j = j + 1
                else:
                    right_pointer = 0
                    down_pointer = 1
                    upper_i = upper_i + 1
                    i = i + 1
            elif down_pointer == 1:
                if i < lower_i:
                    i = i + 1
                else:
                    right_pointer = -1
                    down_pointer = 0
                    right_j = right_j - 1
                    j = j - 1
            elif right_pointer == -1:
                if j > left_j:
                    j = j - 1
                else:
                    right_pointer = 0
                    down_pointer = -1
                    lower_i = lower_i - 1
                    i = i - 1
            elif down_pointer == -1:
                if i > upper_i:
                    i = i - 1
                else:
                    right_pointer = 1
                    down_pointer = 0
                    left_j = left_j + 1
                    j = j + 1
            num = num + 1
        return ans
