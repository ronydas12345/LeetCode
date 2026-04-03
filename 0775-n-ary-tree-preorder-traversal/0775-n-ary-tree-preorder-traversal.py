"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         res = []
#         self.travel(root, res)
#         return res
#     def travel(self, root, res):
#         if not root: return
#         res.append(root.val)
#         for c in root.children: self.travel(c, res)

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        s = [root]
        res = []
        while s:
            peek = s.pop()
            res.append(peek.val)
            s.extend(reversed(peek.children))
        return res
