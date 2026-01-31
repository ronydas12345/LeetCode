# # Recursive
# class Solution:
#     def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
#         if not root: return 0

#         #res = float("inf")
#         def recursive(root, curr):
#             if not root: return curr
#             if root.left: curr = min(abs(root.val - root.left.val), recursive(root.left, curr))
#             if root.right: curr = min(abs(root.val - root.right.val), recursive(root.right, curr))

#             return curr

#         return recursive(root, float("inf"))

# Inorder DFS Recursive
class Solution:
    def getMinimumDifference(self, root):
        global prev
        global res
        prev = None
        res = float("inf")

        def inorder(node):
            global prev
            global res

            if not node:
                return
            inorder(node.left)

            if prev is not None:
                res = min(res, node.val - prev)
            prev = node.val

            inorder(node.right)

        inorder(root)
        return res

# # Inorder Stack
# class Solution:
#     def getMinimumDifference(self, root):
#         s = []
#         cur = root
#         prev = None
#         res = float("inf")

#         while cur or s:
#             while cur:
#                 s.append(cur)
#                 cur = cur.left

#             cur = s.pop()
#             if prev is not None:
#                 res = min(res, cur.val - prev)
#             prev = cur.val

#             cur = cur.right

#         return res

# DFS Space Optimized
# class Solution:
#     def getMinimumDifference(self, root):
#         cur = root
#         prev_val = None
#         ans = float("inf")

#         while cur:
#             if cur.left is None:
#                 if prev_val is not None:
#                     ans = min(ans, cur.val - prev_val)
#                 prev_val = cur.val
#                 cur = cur.right
#             else:
#                 # find predecessor
#                 pre = cur.left
#                 while pre.right and pre.right is not cur:
#                     pre = pre.right

#                 if pre.right is None:
#                     pre.right = cur
#                     cur = cur.left
#                 else:
#                     pre.right = None
#                     if prev_val is not None:
#                         ans = min(ans, cur.val - prev_val)
#                     prev_val = cur.val
#                     cur = cur.right

#         return ans
