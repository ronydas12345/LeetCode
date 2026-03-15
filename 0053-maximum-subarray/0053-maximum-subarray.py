# Brute Force
# class Solution:
#     def maxSubArray(self, nums):
#         n = len(nums)
#         res = float("-inf")

#         for i in range(n):
#             s = 0
#             for j in range(i, n):
#                 s += nums[j]
#                 res = max(res, s)

#         return res

# Brute Force w Cumulative Sum
# class Solution:
#     def maxSubArray(self, nums):
#         n = len(nums)
#         pref = [0] * (n + 1)

#         for i in range(n):
#             pref[i + 1] = pref[i] + nums[i]

#         res = float("-inf")
#         for i in range(n):
#             for j in range(i, n):
#                 sub_sum = pref[j + 1] - pref[i]
#                 res = max(res, sub_sum)

#         return res

# Recursion
class Solution:
    def maxSubArray(self, nums):
        n = len(nums)

        def ending_at(i):
            if i == 0:
                return nums[0]
            return max(nums[i], nums[i] + ending_at(i - 1))

        res = float("-inf")
        for i in range(n):
            res = max(res, ending_at(i))

        return res

# Recursive Memoization
class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        dp = {}

        def ending_at(i):
            if i == 0:
                return nums[0]
            if i in dp:
                return dp[i]

            dp[i] = max(nums[i], nums[i] + ending_at(i - 1))
            return dp[i]

        res = float("-inf")
        for i in range(n):
            res = max(res, ending_at(i))

        return res        

# Iterative
# class Solution:
#     def maxSubArray(self, nums):
#         n = len(nums)
#         dp = [0] * n
#         dp[0] = nums[0]

#         res = dp[0]

#         for i in range(1, n):
#             dp[i] = max(nums[i], nums[i] + dp[i - 1])
#             res = max(res, dp[i])

#         return res

# In Place DP
class Solution:
    def maxSubArray(self, nums):
        res = nums[0]

        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
            res = max(res, nums[i])

        return res