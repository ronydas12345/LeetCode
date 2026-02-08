# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
#         if not nums: return None

#         m = len(nums) // 2
#         root = TreeNode(nums[m])

#         root.left = self.sortedArrayToBST(nums[:m])
#         root.right = self.sortedArrayToBST(nums[m+1:])

#         return root

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums: return None
        
        # init q -> (left, right, parent_node, is_left_child)
        root = TreeNode(0)
        q = collections.deque([(0, len(nums) - 1, root, True)])
        
        while q:
            l, r, parent, is_left = q.popleft()
            mid = (l + r) // 2
            node = TreeNode(nums[mid])
            
            # connect child & parent
            if is_left:
                parent.left = node
            else:
                parent.right = node
            
            # subtrees
            if l <= mid - 1:
                q.append((l, mid - 1, node, True))
            if r >= mid + 1:
                q.append((mid + 1, r, node, False))
                
        return root.left # root.left is acc root