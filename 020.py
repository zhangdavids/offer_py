# 对称的二叉树

class Solution:
    def Symmetrical(self, Lnode, Rnode):
        if Lnode == None and Rnode == None:
            return True
        if Lnode and Rnode:
            return Lnode.val == Rnode.val and self.Symmetrical(Lnode.right, Rnode.left) and self.Symmetrical(Lnode.left,
                                                                                                             Rnode.right)
        else:
            return False

    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        return self.Symmetrical(pRoot.left, pRoot.right)
