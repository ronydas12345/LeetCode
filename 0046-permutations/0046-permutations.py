class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def rec(path, visited):
            if len(path) == len(nums):
                res.append(list(path))
                return
            
            for i in range(len(nums)):
                if visited[i]: continue
                visited[i] = True
                path.append(nums[i])
                rec(path, visited)
                path.pop()
                visited[i] = False
        
        res = []
        rec([], [False] * len(nums))
        return res