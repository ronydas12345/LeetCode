# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: return False
        if head.next is None: return False

        a, b = head, head

        while b and b.next:
            a = a.next
            b = b.next.next

            if a == b: return True
        
        return False
