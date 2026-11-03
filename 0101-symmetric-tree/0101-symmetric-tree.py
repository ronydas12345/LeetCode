# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root: return 

        def check_mirror(p, q):
            if (not p) and (not q): return True
            if (not p) or (not q): return False
            return (p.val == q.val) and (check_mirror(p.left, q.right)) and (check_mirror(p.right, q.left))
    
        return check_mirror(root.left, root.right)