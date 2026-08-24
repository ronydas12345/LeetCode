class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N, M = len(matrix), len(matrix[0])

        l1, r1 = 0, N - 1
        tgt_r = -1

        while l1 <= r1:
            m = l1 + (r1 - l1) // 2

            if matrix[m][0] <= target <= matrix[m][M - 1]:
                tgt_r = m
                break
            elif target < matrix[m][0]:
                r1 = m - 1
            else:
                l1 = m + 1
        
        if tgt_r == -1: return False

        l2, r2 = 0, M - 1
        while l2 <= r2:
            m_c = l2 + (r2 - l2) // 2
            m = matrix[tgt_r][m_c]

            if m == target: return True
            elif m < target: l2 = m_c + 1
            else: r2 = m_c - 1
        
        return False


"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N, M = len(matrix), len(matrix[0])
        l, r = 0, (N * M) - 1

        while l <= r:
            m = l + (r - l) // 2
            r, c = m // M, m % M
            mid = matrix[r][c]

            if mid == target: return True
            elif mid < target: l = m + 1
            else: r = m - 1
        
        return False
"""
