class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n

        a, b, c = 3, 2, 0

        for _ in range(3, n):
            c = a + b
            b = a
            a = c
        
        return c