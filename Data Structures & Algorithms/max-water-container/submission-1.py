class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #use two pointer algorithm 
        #compute height
        #move the one with the smaller height  

        best = 0 

        left = 0 
        right = len(heights) - 1 

        while left < right: 
            height = max(heights[left], heights[right]) * (right - left)
            best = max (height, best) 

            if heights[left] < heights[right]: 
                left += 1 
            else: 
                right -= 1 


        return best
    
        