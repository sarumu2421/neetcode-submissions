class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0 
        right = rows*cols - 1

        while left <= right: 
            midpoint = left + (right - left) // 2
            mid_val = matrix[midpoint // cols][midpoint % cols] 
            
            if mid_val == target:
                return True
            elif mid_val > target:
                right = midpoint - 1
            else:
                left = midpoint + 1

        return False


        