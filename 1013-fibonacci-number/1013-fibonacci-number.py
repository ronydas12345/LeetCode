class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n

        m = [0] * (n + 1)
        m[1] = 1

        for i in range(2, n + 1):
            m[i] = m[i - 1] + m[i - 2]
        
        return m[n]

        """
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
        """