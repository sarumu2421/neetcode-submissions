class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0

        l = 0 
        r = 1   

        while r < len(prices): 
            if prices[r] > prices[l]: 
                max_prof = max(prices[r] - prices[l], max_prof) 
                right += 1
            else: 
                left = right 
                right += 1 

        return max_prof






        