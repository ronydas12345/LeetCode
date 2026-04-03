"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

# class Solution:
#     def postorder(self, root: 'Node') -> List[int]:
#         def rec(root):
#             if not root: return
#             for n in root.children:
#                 rec(n)
#                 res.append(n.val)
    
#         res = []
#         if not root: return []
#         rec(root)
#         res.append(root.val)
#         return res

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return []
        res, s = [], [root]
        while s:
            peek = s.pop()
            res.append(peek.val)
            s.extend(peek.children)
        return res[::-1]
