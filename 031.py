class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1== None or pHead2 == None:
            return None
        pa = pHead1
        pb = pHead2
        while(pa!=pb):
            pa = pHead2 if pa is None else pa.next
            pb = pHead1 if pb is None else pb.next
        return pa