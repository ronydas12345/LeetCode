# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return None
        if head.next is None: return None

        a, b = head, head

        while b and b.next:
            a = a.next
            b = b.next.next

            if a == b:
                a = head
                while a != b:
                    a = a.next
                    b = b.next

                return a
        
        return None