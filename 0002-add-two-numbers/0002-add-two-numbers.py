# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#     def get_val(self):
#         return self.val
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digit, res = 0, ListNode(0)
        last = res
        while l1 or l2 or digit:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            s = v1 + v2 + digit
            digit = s // 10

            #res = self.append_node(res, s % 10, last)
            
            last.next = ListNode(s % 10)

            last = last.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return res.next
