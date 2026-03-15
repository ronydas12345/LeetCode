class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]

        def rec(x, y):
            if x < 0 or x >= len(image): return
            if y < 0 or y >= len(image[0]): return
            
            if image[x][y] == color: return
            if image[x][y] != start: return
            
            image[x][y] = color

            rec(x - 1, y)
            rec(x + 1, y)
            rec(x, y + 1)
            rec(x, y - 1)
        
        rec(sr, sc)
        return image