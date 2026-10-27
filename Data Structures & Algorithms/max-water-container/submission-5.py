class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1 
        maxArea = 1

        while l < r: 
            num = min(heights[l], heights[r])
            currArea = num * (r - l)
            maxArea = max(maxArea, currArea) 

            if heights[l] < heights[r]: 
                l += 1 
            else: 
                r -= 1

        return maxArea
