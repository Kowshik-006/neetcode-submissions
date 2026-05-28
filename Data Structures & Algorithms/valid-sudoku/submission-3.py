class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            set_row = set()
            for j in range(9):
                if board[i][j] in set_row:
                    return False
                elif board[i][j] != ".":
                    set_row.add(board[i][j])
        
        for j in range(9):
            set_col = set()
            for i in range(9):
                if board[i][j] in set_col:
                    return False
                elif board[i][j] != ".":
                    set_col.add(board[i][j])
        
        for square in range(9):
            set_square = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] in set_square:
                        return False
                    elif board[row][col] != ".":
                        set_square.add(board[row][col])
        
        return True












