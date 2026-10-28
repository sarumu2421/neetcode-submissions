class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = [1] * n 

        for i in range(m - 1): #going through all the rows except for the last since we know thats all ones 
            newRow = [1] * n # same dimensions as other row
            for j in range(n - 2, -1, -1): 
                newRow[j] = newRow[j + 1] + rows[j]
            rows = newRow  
        
        return rows[0]
            