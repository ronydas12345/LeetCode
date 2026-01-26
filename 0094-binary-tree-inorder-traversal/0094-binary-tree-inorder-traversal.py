# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursive(self, root, res):
        if root.left: self.recursive(root.left, res)

        res.append(root.val)

        if root.right: self.recursive(root.right, res)

        return res
            

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            return self.recursive(root, [])
        else:
            return []