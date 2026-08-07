class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        max_area = 0

        while left < right: 
            mini = min(heights[left], heights[right])
            area = (right-left) * mini
            max_area = max(max_area, area)

            if heights[left] < heights[right]: 
                left += 1
            elif heights[right] < heights[left]: 
                right -= 1 
            else: 
                if heights[left+1] > heights[right-1]:
                    left += 1
                else: 
                    right -= 1

            
        return max_area
            

        