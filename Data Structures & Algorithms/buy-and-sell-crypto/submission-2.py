class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy it at the lowest one in the beginning and sell at the highest towards the end 
        # i < j
        #two pointers 
        profit = 0 
        lowest = prices[0]

        if len(prices) == 1: 
            return profit

        left = 0 
        right = 1

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = max(profit, prices[right] - prices[left])

            right += 1

        return profit
        