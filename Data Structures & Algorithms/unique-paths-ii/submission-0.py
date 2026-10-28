class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[1] * rows for _ in range(cols)]

        for r in range(1, rows): 
            for c in range(1, cols): 
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0 
                else: 
                    dp[r][c] = dp[r-1][c] + dp[r][c-1] 
    
        return dp[rows - 1][cols - 1]



        