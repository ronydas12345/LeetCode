# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid, end = head, head
        while end is not None and end.next is not None:
            mid = mid.next
            end = end.next.next
        
        return mid