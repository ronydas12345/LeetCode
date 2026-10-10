class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        for r in range(9):
            for c in range(9):
                v = board[r][c]

                if v == ".": continue

                for j in range(9):
                    if j != c and board[r][j] == v: return False

                for i in range(9):
                    if i != r and board[i][c] == v: return False
                
                box_r_start = (r // 3) * 3
                box_c_start = (c // 3) * 3

                for k in range(box_r_start, box_r_start + 3):
                    for l in range(box_c_start, box_c_start + 3):
                        if k != r and l != c and board[k][l] == v: return False
        
        return True
            
                