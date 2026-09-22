class Solution:
    # def isPowerOfTwo(self, n: int) -> bool:
    #     if n <= 0: return False
    #     if n == 1: return True
    #     if n % 2: return False

    #     return self.isPowerOfTwo(n // 2)

    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        return n & (n - 1) == 0
    
    """
     2 -> 10
     4 -> 100
     8 -> 1000
    16 -> 10000

     1 -> 01
     3 -> 011
     7 -> 0111
    15 -> 01111
    ...
    """