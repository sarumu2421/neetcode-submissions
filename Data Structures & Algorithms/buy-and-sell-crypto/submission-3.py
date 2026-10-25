class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0

        left = 0 
        right = 1   

        while r < len(prices): 
            if price[r] > prices[l]: 
                max_prof = max(price[r] - prices[l], max_prof) 
                right += 1
            else: 
                left = right 
                right += 1 
                
        return max_prof






        