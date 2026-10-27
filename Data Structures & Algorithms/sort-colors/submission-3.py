class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #2 PASS SOLUTION

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

   

        # #1 PASS SOLUTION  

        # l = 0 
        # r = len(nums) - 1
        # curr = 0


        # while curr <= r: 
        #     if nums[curr] == 0: 
        #         nums[l], nums[curr] = nums[curr], nums[l]
        #         l += 1 
        #         curr += 1
            
        #     elif nums[curr] == 2: 
        #         nums[r], nums[curr] = nums[curr], nums[r]
        #         r -= 1 

        #     else:
        #         curr += 1


        