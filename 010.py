# 平衡二叉树

class Solution:
    def Treeheight(self,pRoot):
        if pRoot == None:
            return 0
        if pRoot.left == None and pRoot.right == None:
            return 1
        lh = self.Treeheight(pRoot.left)
        rh = self.Treeheight(pRoot.right)
        return max(rh,lh)+1

    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        return abs(self.Treeheight(pRoot.left)-self.Treeheight(pRoot.right))<=1