# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root: return 0

    #     s = [(root, 1)]
    #     res = 0

    #     while s:
    #         node, depth = s.pop()
    #         res = max(res, depth)

    #         if node.left:
    #             s.append((node.left, depth + 1))
    #         if node.right:
    #             s.append((node.right, depth + 1))
        
    #     return res

    def recursive(self, root, depth):
        if not root: return 0
        left, right = depth, depth

        if root.left:
            left = self.recursive(root.left, depth + 1)
        if root.right:
            right = self.recursive(root.right, depth + 1)
        
        return max(left, right)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursive(root, 1)