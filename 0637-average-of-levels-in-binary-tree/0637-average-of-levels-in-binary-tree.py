# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []

        res, q = [], [root]

        while q:
            cur_sum, cur_len = 0, len(q)

            for _ in range(cur_len):
                n = q.pop()
                cur_sum += n.val

                if n.left: q.insert(0, n.left)
                if n.right: q.insert(0, n.right)
            
            res.append(cur_sum / cur_len)
        
        return res
