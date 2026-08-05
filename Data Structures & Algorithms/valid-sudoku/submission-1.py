class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check all row:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                
                seen.add(board[row][i])

        # check all columns:
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                
                seen.add(board[i][col])
        
        for square_box in range(9):
            seen = set()
            for i in range(3):
                # compute
                for j in range(3): 

                    row = (square_box // 3)*3 + i
                    col = (square_box % 3)*3 + j

                    if board[row][col] == '.':
                       continue
                    if board[row][col] in seen:
                       return False
                
                    seen.add(board[row][col])
        return True