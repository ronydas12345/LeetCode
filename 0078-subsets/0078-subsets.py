class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res, subset, N = [], [], len(nums)

        def rec(i):
            if i >= N:
                res.append(subset.copy())
                return
            
            #include nums[i]
            subset.append(nums[i])
            rec(i + 1)

            #exclude nums[i] then backtrack
            subset.pop()
            rec(i + 1)
        
        rec(0)
        return res
