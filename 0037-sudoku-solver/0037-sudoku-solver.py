
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        N = 9

        def solve():
            min_count = 10
            best_cell = None
            best_candidates = []

            for r in range(N):
                for c in range(N):
                    if board[r][c] == ".":
                        candidates = []

                        for i in range(1, 10):
                            if isValidSudoku(r, c, str(i)):
                                candidates.append(str(i))

                        if len(candidates) == 0:
                            return False

                        if len(candidates) < min_count:
                            min_count = len(candidates)
                            best_cell = (r, c)
                            best_candidates = candidates

                        if min_count == 1:
                            break
                if min_count == 1:
                    break

            if best_cell is None:
                return True

            r, c = best_cell

            for ch in best_candidates:
                board[r][c] = ch

                if solve():
                    return True

                board[r][c] = "."

            return False

        def isValidSudoku(r, c, ch) -> bool:
            for i in range(9):
                if board[i][c] == ch:
                    return False
                if board[r][i] == ch:
                    return False

                if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == ch:
                    return False

            return True

        solve()
