# 二叉平衡树中的第k小数

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        stack = []
        node = pRoot
        while node:
            stack.append(node)
            node = node.left
        cnt = 1
        while (stack and cnt <= k):
            node = stack.pop()
            right = node.right
            while right:
                stack.append(right)
                right = right.left
            cnt += 1
        if node and k == cnt - 1:
            return node
        return None
