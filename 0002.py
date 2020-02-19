# 链表中环的入口节点

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


class Solution2:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return None
        fast = slow = pHead
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = pHead
                while (fast != slow):
                    fast = fast.next
                    slow = slow.next
                return fast
        return None
