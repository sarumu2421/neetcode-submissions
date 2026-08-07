class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        output = [] 

        for i in range(len(nums)): 
            product = 1
            for j in range(len(nums)): 
                if j == i: 
                    j += 1 
                product *= j  
            output.append(product) 
        
        return output
        