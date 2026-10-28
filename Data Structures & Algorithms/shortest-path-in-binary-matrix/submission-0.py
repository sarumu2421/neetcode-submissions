class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque

        rows = len(grid)
        cols = len(grid[0]) 

        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1
 
        q = deque([(0, 0)]) 
        grid[0][0] = 2
        length = 1

        while q: 
            for _ in range(len(q)):
                r,c = q.popleft() 
                if (r,c) == (rows-1, cols-1): 
                    return length
                directions = [(r+1, c), (r-1, c), (r, c+1), (r, c-1),
              (r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1)]

                for row, col in directions: 
                    if row >= 0 and row < rows and col >=0 and col < cols and grid[row][col] == 0: 
                        grid[row][col] = 2 #2 means alr visited
                        q.append((row, col))

            length += 1
        
        return -1 

        