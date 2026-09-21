class Solution:
    def jump(self, nums: list[int]) -> int:
        N = len(nums)
        max_dist, curr_end, res = 0, 0, 0
        
        for i in range(N - 1):
            max_dist = max(max_dist, i + nums[i])

            if i == curr_end:
                res += 1
                curr_end = max_dist
        
        return res
