class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #remove neg prefix 
        #sliding window 

        maxSub = nums[0]
        currSum = 0 


        #go through entire array once 
        for n in nums: 
            if currSum < 0: 
                currSum = 0
            currSum += n  
            maxSub = max(maxSub, currSum)

        return maxSub
        