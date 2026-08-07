class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        results = set() #for fast checking

        for i in range(len(nums)):   
            left = 0 
            right = len(nums) - 1 

            if nums[i] + nums[left] + nums[right] == 0: 
                result = tuple(sorted([nums[i],nums[left],nums[right]]))
                results.add(result)  
            
            left += 1
            right -= 1
            
        final = [list(t) for t in results] #convert back to array 
        return final
        

            