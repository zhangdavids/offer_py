class Solution:
    def multiply(self, A):
        # write code here
        size = len(A)
        B = [1]*size
        for i in range(1,size):
            B[i] = B[i-1]*A[i-1]
        tmp = 1
        for i in range(size-2,-1,-1):
            tmp = tmp*A[i+1]
            B[i] = B[i]*tmp
        return B