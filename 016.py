# -*- coding:utf-8 -*-

# 二叉树的深度


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
        if pRoot.left is None and pRoot.right is None:
            return 1
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1
