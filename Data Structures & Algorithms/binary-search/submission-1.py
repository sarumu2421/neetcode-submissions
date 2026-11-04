class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1 

        while left <= right: 
            midpoint = left + (right - left)//2 
            midval = nums[midpoint] 

            if target == midval: 
                return midpoint 
            elif target < midval: 
                right = midpoint - 1 
            else: 
                left = midpoint + 1 
            
        return -1
        