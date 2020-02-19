# 删除链表中重复的节点

class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        pos = pHead
        ret = ListNode(-1)
        tmp = ret
        flag = False
        while (pos and pos.next):
            if pos.val == pos.next.val:
                flag = True
                pos.next = pos.next.next
            else:
                if flag:
                    flag = False
                else:
                    tmp.next = ListNode(pos.val)
                    tmp = tmp.next
                pos = pos.next
        if pos and flag == False:
            tmp.next = ListNode(pos.val)
        return ret.next
