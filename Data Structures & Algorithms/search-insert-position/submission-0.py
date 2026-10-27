class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1 

        while left <= right: 
            midpoint = left + (right - left)// 2 
            mid_val = nums[midpoint]


            if mid_val == target: 
                return midpoint
            elif mid_val > target: 
                right = midpoint - 1
            else: 
                left = midpoint + 1 

            
        return left
        