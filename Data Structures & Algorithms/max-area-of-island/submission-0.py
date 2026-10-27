class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area = 0 
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c): 
            directions = [(r, c+1), (r, c-1), (r+1, c), (r-1, c)] 

            if r < 0 or r >= rows or c < 0 or c >= cols: 
                return 0

            if grid[r][c] != 1:
                return 0

            if grid[r][c] == 1: 
                curr_area = 1
                grid[r][c] = 2
                for row, col in directions: 
                    curr_area += dfs(row, col)
            
                return curr_area


        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 1: 
                    max_area = max(max_area, dfs(r, c))

        return max_area 

        