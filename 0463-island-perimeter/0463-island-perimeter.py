class Solution:
    def islandPerimeter(self, grid):
        if not grid or not grid[0]:
            return 0

        N = len(grid)
        M = len(grid[0])

        # scan for first land cell
        start = None
        for r in range(N):
            for c in range(M):
                if grid[r][c] == 1:
                    start = (r, c)
                    break
            if start:
                break

        if not start:
            return 0

        # pop in O(1)
        q = [start]
        front = 0

        # start is visited
        sr, sc = start
        grid[sr][sc] = float("inf")

        res = 0

        while front < len(q):
            r, c = q[front]
            front += 1

            # down
            nr, nc = r + 1, c
            if nr >= N:
                res += 1
            elif grid[nr][nc] == 0:
                res += 1
            elif grid[nr][nc] == 1:
                grid[nr][nc] = float("inf")
                q.append((nr, nc))

            # up
            nr, nc = r - 1, c
            if nr < 0:
                res += 1
            elif grid[nr][nc] == 0:
                res += 1
            elif grid[nr][nc] == 1:
                grid[nr][nc] = float("inf")
                q.append((nr, nc))

            # right
            nr, nc = r, c + 1
            if nc >= M:
                res += 1
            elif grid[nr][nc] == 0:
                res += 1
            elif grid[nr][nc] == 1:
                grid[nr][nc] = float("inf")
                q.append((nr, nc))

            # left
            nr, nc = r, c - 1
            if nc < 0:
                res += 1
            elif grid[nr][nc] == 0:
                res += 1
            elif grid[nr][nc] == 1:
                grid[nr][nc] = float("inf")
                q.append((nr, nc))

        return res