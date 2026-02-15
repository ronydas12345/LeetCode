# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        height, curr = 0, root
        while curr.left: # get max height
            curr = curr.left
            height += 1
        
        max_i = 2 ** height

        # check leaf @ bottom exists [1...2^h]
        def exists(leaf):
            curr = root
            l, r = 1, max_i
            while l < r:
                m = (l + r) // 2
                if leaf > m:
                    curr = curr.right
                    l = m + 1
                else:
                    curr = curr.left
                    r = m
            return curr != None
        
        # bin search # leaver at bottom

        l, r = 1, max_i
        while l <= r:
            m = (l + r) // 2
            if exists(m): l = m + 1
            else: r = m - 1
        
        # 2**height -> # nodes in tree w/o bottom
        #         r -> leaves at bottom
        return 2 ** height + r - 1