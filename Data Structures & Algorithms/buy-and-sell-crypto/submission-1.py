class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy it at the lowest one in the beginning and sell at the highest towards the end 
        # i < j
        #two pointers 
        profit = 0

        if len(prices) == 1: 
            return 0

        lowest = prices[0] 

        for i in range(1, len(prices)): 
            if (prices[i] - lowest) > profit:
                profit =  prices[i] - lowest 
            lowest = min(prices[i], lowest)
            

        return profit

        