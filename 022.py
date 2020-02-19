# 按之字形顺序打印二叉树

class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        stack = [pRoot]
        step = 1
        ret = []
        while (stack):
            tmpstack = []
            tmp = []
            for node in stack:
                tmp += [node.val]
                if node.left:
                    tmpstack.append(node.left)
                if node.right:
                    tmpstack.append(node.right)
            if step % 2 == 0:
                tmp.reverse()
            ret.append(tmp)
            step += 1
            stack = tmpstack[:]
        return ret
