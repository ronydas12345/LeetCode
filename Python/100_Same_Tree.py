# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def compare(p, q):
            if p is None and q is None: return True
            if p and q and p.val == q.val: return compare(p.left, q.left) and compare(p.right, q.right)
            return False
        
        return compare(p, q)