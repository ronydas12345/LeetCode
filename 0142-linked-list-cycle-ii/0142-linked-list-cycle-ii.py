# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        visited = set()
        while i:
            if i in visited:
                return i
            visited.add(i)
            i = i.next
        return None