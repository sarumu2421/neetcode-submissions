class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        currProd = 1 

        for n in nums: 
            currProd *= n
            maxProd = max(maxProd, currProd)
        return maxProd
        