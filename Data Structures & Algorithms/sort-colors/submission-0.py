class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #3-pointer solution

        l = 0 
        zeros = 0
        
        for r in range(len(nums)): 
            if nums[r] == 0: 
                nums[l], nums[r] = nums[r], nums[l]
                zeros += 1
                l += 1 
            
        for r in range(zeros, len(nums)): 
            if nums[r] == 1: 
                nums[l], nums[r] = nums[r], nums[l]
                l += 1 
        