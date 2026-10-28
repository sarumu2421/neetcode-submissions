class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0] * cols for _ in range(rows)]

        # first row: 1s until you hit an obstacle
        for c in range(cols):
            if obstacleGrid[0][c] == 1:
                break
            dp[0][c] = 1

        # first column: 1s until you hit an obstacle
        for r in range(rows):
            if obstacleGrid[r][0] == 1:
                break
            dp[r][0] = 1

        for r in range(1, rows): 
            for c in range(1, cols): 
                if obstacleGrid[r][c] == 0:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1] 
    
        return dp[rows - 1][cols - 1]



        