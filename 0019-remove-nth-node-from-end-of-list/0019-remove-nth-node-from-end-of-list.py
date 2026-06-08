# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a, b, l = head, head, 1
        for i in range(n):
            b = b.next

        if b is None: return head.next
        
        while b.next is not None:
            b = b.next
            a = a.next
            l += 1

        
        a.next = a.next.next
        return head