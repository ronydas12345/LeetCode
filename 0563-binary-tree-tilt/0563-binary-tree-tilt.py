# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        stack = [(root, False)]
        node_to_sum = {}

        while stack:
            node, visited = stack.pop()

            if node is None:
                continue

            if visited:
                left = node_to_sum.get(node.left, 0)
                right = node_to_sum.get(node.right, 0)
                res += abs(left - right)
                node_to_sum[node] = node.val + left + right
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return res
