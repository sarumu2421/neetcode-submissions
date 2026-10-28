class Solution:
    def solve(self, board: List[List[str]]) -> None: 
        #DFS 
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c): 
            directions = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O": 
                return  
            
            board[r][c] = "T"   
            
            for row, col in directions: 
                dfs(row, col) 
            


        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:   # border only
                    dfs(r, c) 

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
        