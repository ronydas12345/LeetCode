class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        m, res, i = 1, 0, 0

        while m <= n:
            if i < len(nums) and nums[i] <= m:
                m += nums[i]
                i += 1
            else:
                m <<= 1
                res += 1

        return res