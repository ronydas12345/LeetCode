class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1]]
        if numRows == 1: return [[1]]
        if numRows == 2: return [[1], [1, 1]]

        for i in range(3, numRows + 1):
            res.append([0] * i)
            res[i - 1][0] = 1
            res[i - 1][i - 1] = 1

            for j in range(1, i - 1):
                res[i - 1][j] = res[i - 2][j - 1] + res[i - 2][j]

        return res

"""
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
"""