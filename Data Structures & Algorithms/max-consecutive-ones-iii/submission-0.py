class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0 
        zeros = 0 
        max_window = 0 

        for r in range(len(nums)): 
            if nums[r] == 0: 
                zeros += 1 
        
            while zeros > k: 
                if nums[l] == 0:
                    zeros -= 1 
                l += 1 

            max_window = max(max_window, r - l + 1) 

        return max_window


        