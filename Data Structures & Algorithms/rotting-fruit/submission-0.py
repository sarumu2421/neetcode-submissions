class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        fresh = 0 
        mins = 0

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 2: 
                    q.append((r,c)) 
                if grid[r][c] == 1: 
                    fresh += 1

        while q and fresh > 0: 
            for _ in range(len(q)): 
                r, c = q.popleft() 
                dir = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for row, col in dir: 
                    if row >= 0 and row < rows and col >= 0 and col < cols and grid[row][col] == 1: 
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1 

            mins += 1

            
        if fresh == 0: 
            return mins 
        else: 
            return -1

                

        