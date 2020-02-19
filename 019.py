# 二叉树的下一个节点

class Solution:
    def GetNext(self, pNode):
        # write code here
        # left root right
        if pNode == None:
            return None
        if pNode.right:
            tmp = pNode.right
            while (tmp.left):
                tmp = tmp.left
            return tmp
        p = pNode.next
        while (p and p.right == pNode):
            pNode = p
            p = p.next
        return p
