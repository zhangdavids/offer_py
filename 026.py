class Solution(object):
    # 中序和先序
    def buildTree(self, pre, tin):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if pre == []:
            return None
        val = pre[0]
        idx = tin.index(val)
        ltin = tin[0:idx]
        rtin = tin[idx + 1:]
        lpre = pre[1:1 + len(ltin)]
        rpre = pre[1 + len(ltin):]
        root = TreeNode(val)
        root.left = self.buildTree(lpre, ltin)
        root.right = self.buildTree(rpre, rtin)
        return root

    # 中序和后序
    def buildTree2(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if postorder == []:
            return None
        val = postorder[-1]
        idx = inorder.index(val)
        lin = inorder[0:idx]
        rin = inorder[idx + 1:]
        lpos = postorder[0:len(lin)]
        rpos = postorder[len(lin):-1]
        root = TreeNode(val)
        root.left = self.buildTree(lin, lpos)
        root.right = self.buildTree(rin, rpos)
        return root
