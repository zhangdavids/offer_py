# 从尾到头打印链表

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        ret = []
        head = listNode
        while(head):
            ret.append(head.val)
            head = head.next
        ret.reverse()
        return ret