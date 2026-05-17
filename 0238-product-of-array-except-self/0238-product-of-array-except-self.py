class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0] * N

        be = af = 1

        for i in range(N):
            res[i] = be
            be *= nums[i]
        
        for i in range(N - 1, -1, -1):
            res[i] *= af
            af *= nums[i]
        
        return res
        