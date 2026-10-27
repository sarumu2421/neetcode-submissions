class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = max(nums)
        currMin = 1 
        currMax = 1

        for n in nums: 
            if n == 0: 
                currMin = 1
                currMax = 1
                continue
            
            temp = currMax * n
            currMax = max(n*currMax, n*currMin, n)
            currMin = min(temp, n*currMin, n)
            
            maxProd = max(maxProd, currMin, currMax)

        return maxProd
        