class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1

        while left < right: 
            mini = min(heights[left], heights[right])
            area = (right-left) * mini

            if heights[left] < heights[right] and heights[left+1] > heights[left]: 
                left += 1
            elif heights[right] < heights[left]and heights[right-1] > heights[right]: 
                right -= 1
            else: 
                return area
            

        