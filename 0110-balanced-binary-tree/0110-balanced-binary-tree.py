# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def check_root(root):
            if not root: return 0

            l_ht = check_root(root.left)
            if l_ht <= -1: return -1

            r_ht = check_root(root.right)
            if r_ht <= -1: return -1

            if abs(l_ht - r_ht) > 1: return -1

            return max(l_ht, r_ht) + 1

        return check_root(root) != -1