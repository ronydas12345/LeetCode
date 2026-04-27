class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t, b = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        res, area = [], (b + 1) * (r + 1)

        # left  : 1
        # down  : 2
        # right : 3
        # up    : 4

        while len(res) < area:
            print(t, b, l, r)

            #top
            #res.extend(matrix[t][l : r + 1])
            for i in range(l, r + 1): res.append(matrix[t][i])
            t += 1
        
            #right
            for i in range(t, b + 1): res.append(matrix[i][r])
            r -= 1

            if t <= b:
                #bottom
                #res.extend(matrix[b][r : l : -1])
                for i in range(r, l - 1, -1): res.append(matrix[b][i])
                b -= 1

            if l <= r:
                #left
                for i in range(b, t - 1, -1): res.append(matrix[i][l])
                l += 1


        return res