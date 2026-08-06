class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        #naive method O(n^2)
        # output = [] 

        # for i in range(len(nums)): 
        #     product = 1

        #     for j in range(len(nums)): 
        #         if j != i: 
        #             product *= nums[j]

        #     output.append(product) 
        
        # return output 

        #CORRECT SOLUTION O(n), precompute products to left of i and products to right of i 
        output = [1] * len(nums) 

        #first pass, store left products in output 
        prefix = 1 
        for i in range(len(nums)): 
            output[i] *= prefix
            prefix *= nums[i] 
        
        #second pass, store right products in output (multiplies by left products alr stored in array)
        suffix = 1 
        for i in range(len(nums) - 1, -1, -1): 
            output[i] *= suffix
            suffix *= nums[i]  

        return output
