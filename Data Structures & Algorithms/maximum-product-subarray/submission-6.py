class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = max(nums)
        currMin = 1 
        currMax = 1

        for n in nums: 
            temp = currMax * n
            currMax = max(n*currMax, n*currMin, n)
            currMin = min(temp, n*currMin, n)
            
            maxProd = max(maxProd, currMax)

        return maxProd
        