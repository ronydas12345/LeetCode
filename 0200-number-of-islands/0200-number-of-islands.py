class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        pos, queue, visited, res = (0, 0), [], set(), 0

        def explore():
            while queue:
                x, y = queue.pop()
                for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    nxt = (x + dx, y + dy)
                    if 0 <= nxt[0] < len(grid) and 0 <= nxt[1] < len(grid[0]):
                        if nxt not in visited and grid[nxt[0]][nxt[1]] == "1":
                            visited.add(nxt)
                            queue.append(nxt)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x, y) not in visited and grid[x][y] == "1":
                    queue.append((x, y))
                    visited.add((x, y))
                    explore()
                    res += 1

        return res

#Time/Space: O(n^2)