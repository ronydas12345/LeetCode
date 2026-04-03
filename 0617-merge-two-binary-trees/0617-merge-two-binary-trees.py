# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
#         if root1 and root2:
#             root = TreeNode(root1.val + root2.val)
#             root.right = self.mergeTrees(root1.right, root2.right)
#             root.left = self.mergeTrees(root1.left, root2.left)
#             return root
#         else:
#             if root1 and root2: return root1
#             elif root2: return root2
#             elif root1: return root1
#             else: return None

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1: return root2
        s = [(root1, root2)]
        while s:
            a, b = s.pop()
            if not a or not b: continue

            a.val += b.val

            if not a.left: a.left = b.left
            else: s.append((a.left, b.left))

            if not a.right: a.right = b.right
            else: s.append((a.right, b.right))
        
        return root1
    