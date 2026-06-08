# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l, a = 0, head
        while a.next is not None:
            a = a.next
            l += 1

        a, at = head, 0
        while at < math.ceil(l / 2):
            at += 1
            a = a.next
        
        return a
