class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        start, flag = (-1, -1), False

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    start, flag = (r, c), True
                    break
            if flag: break

        q, visited, res = [start], [], 0

        while q:"""

        print(self.in_bounds(grid, 0, 5))

        dirs = ((-1, 0), (0, -1), (1, 0), (0, 1))

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    for d in dirs:
                        i, j = r + d[0], c + d[1]
                        if self.in_bounds(grid, i, j) or grid[i][j] == 0: res += 1

                    """
                if grid[r][c] == 1:
                    if self.in_bounds(grid, r - 1, c) or grid[r - 1][c] == 0: res += 1
                    if self.in_bounds(grid, r, c - 1) or grid[r][c - 1] == 0: res += 1
                    if self.in_bounds(grid, r + 1, c) or grid[r + 1][c] == 0: res += 1
                    if self.in_bounds(grid, r, c + 1) or grid[r][c + 1] == 0: res += 1"""
        
        return res
    
    def in_bounds(self, grid, r, c): 
        return (r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]))
    