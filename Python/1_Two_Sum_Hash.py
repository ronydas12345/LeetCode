class Solution:
    def twoSum(self, nums, target):
        m = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in m:
                return [m[comp], i]
            m[num] = i