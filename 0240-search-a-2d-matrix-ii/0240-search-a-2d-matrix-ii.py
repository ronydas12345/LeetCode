class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N, M = len(matrix[0]), len(matrix)
        r, c = 0, N - 1

        while c >= 0 and r < M:
            if matrix[r][c] == target: return True
            elif matrix[r][c] < target: r += 1
            else: c -= 1
        
        return False