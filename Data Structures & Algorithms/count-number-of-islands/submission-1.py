class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            directions = [(r, c+1), (r, c-1), (r+1, c), (r-1, c)]

            if r < 0 or r >= rows or c < 0 or c >= cols: 
                return #water

            if grid[r][c] != "1": 
                return #water 

            if grid[r][c] == "1":
                grid[r][c] = "#" #shows we've visited it before
                for row, col in directions: 
                    dfs(row, col)

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands

        