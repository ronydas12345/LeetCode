# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root: return []

        res, q, d = [], [root], 1

        while q:
            size = len(q)
            nodes = []

            for _ in range(size):
                node = q.pop(0)
                nodes.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            if d <= -1:
                nodes = nodes[::-1]
            
            res.append(nodes)
            d *= -1
        
        return res