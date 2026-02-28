# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = {}
        def dfs(root):
            if not root: return

            freq[root.val] = freq.get(root.val, 0) + 1
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        mx = max(freq.values())

        return [k for k in freq if freq[k] == mx]