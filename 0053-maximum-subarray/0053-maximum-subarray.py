class Solution:
    #memoization
    def maxSubArray(self, nums):
        n = len(nums)
        dp = {}

        def ending_at(i):
            if i == 0: return nums[0]
            if i in dp: return dp[i]

            dp[i] = max(nums[i], nums[i] + ending_at(i - 1))
            return dp[i]

        res = float("-inf")
        for i in range(n):
            res = max(res, ending_at(i))
        return res