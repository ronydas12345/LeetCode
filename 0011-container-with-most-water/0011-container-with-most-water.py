class Solution:
    def maxArea(self, height: List[int]) -> int:
        a, b = 0, len(height) - 1
        res = 0
        while b > a:
            res = max(res, min(height[a], height[b]) * (b - a))

            if height[a] > height[b]: b -= 1
            else: a += 1
        
        return res