# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def search(node):
            if not node: return (True, 0)
        
            left_balance, left_ht = search(node.left)
            right_balance, right_ht = search(node.right)

            balance = left_balance and right_balance and abs(left_ht - right_ht) <= 1

            return (balance, 1 + max(left_ht, right_ht))
        
        return search(root)[0]