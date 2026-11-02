class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        print(board)

        col = set()
        diag_pos = set()
        diag_neg = set()

        def rec(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return

            for c in range(n):
                if c in col or (r + c) in diag_pos or (r - c) in diag_neg:
                    continue
                
                col.add(c)
                diag_pos.add(r + c)
                diag_neg.add(r - c)
                board[r][c] = 'Q'

                rec(r + 1)

                col.remove(c)
                diag_pos.remove(r + c)
                diag_neg.remove(r - c)
                board[r][c] = '.'

        rec(0)
        return res


