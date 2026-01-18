class Solution:
    def maxArea(self, height: List[int]) -> int:
        a, b, res = 0, len(height) - 1, 0

        while a < b:
            min_wall, dist = min(height[a], height[b]), b - a
            v = dist * min_wall
            
            if height[a] < height[b]: a += 1
            else: b -= 1

            res = max(res, v)
        
        return res