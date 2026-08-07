class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        results = set() #for fast checking for unique arrays

        for i in range(len(nums)): 
            if nums[i] == nums[i-1]: #skips duplicates
                continue  

            left = i + 1 #bc i is already as lowest/as negative as it can be, you dont wanna add more neg numbers to it bc that wont get to 0
            right = len(nums) - 1 #end of array

            while left < right: 
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0: 
                    result = tuple(sorted([nums[i],nums[left],nums[right]]))
                    results.add(result) 
                    break 
                elif sum > 0: 
                    right -= 1
                elif sum < 0:
                    left += 1


        final = [list(t) for t in results] #convert back to array 
        return final
        

            