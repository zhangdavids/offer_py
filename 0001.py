# coding: utf-8

# 二叉树的镜像


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root is None:
            return
        self.Mirror(root.left)
        self.Mirror(root.right)
        root.left, root.right = root.right, root.left
