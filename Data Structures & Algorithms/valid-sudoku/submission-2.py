class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Possible numbers in a cell: 1-9
        # We can represent 1-9 using a 9 bit binary value
        # 9 bit binary => bit 0 to bit 8
        # value => (value - 1)th bit set to 1
        # Or,simply, value => 1 << (value - 1)
        # We can represent a row/column/square using a 9 bit binary value
        # If nth bit is set, that means n+1 is present

        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                to_be_shifted = int(board[row][col]) - 1

                if rows[row] & (1 << to_be_shifted):
                    return False
                if cols[col] & (1 << to_be_shifted):
                    return False
                if squares[(row//3)*3 + (col//3)] & (1 << to_be_shifted):
                    return False

                rows[row] |= (1 << to_be_shifted)
                cols[col] |= (1 << to_be_shifted)
                squares[(row//3)*3 + (col//3)] |= (1 << to_be_shifted)
        
        return True
