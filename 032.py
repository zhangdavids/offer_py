# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        queue = []
        memories = dict()
        for idx,char in enumerate(s):
            if char not in memories:
                queue.append(idx)
                memories[char]=0
            memories[char]+=1
            while(queue and memories[s[queue[0]]]>1):
                queue.pop(0)
        return queue[0] if queue else -1