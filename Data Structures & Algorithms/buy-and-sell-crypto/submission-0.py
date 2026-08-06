class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #find min price and buy on that day 
        #track each day from there to sell return the max difference 
        #also update min is curr price is smaller 

        min_price = 1000
        max_profit = 0 

        for price in prices: 
            if price < min_price: 
                min_price = price 
            else: 
                if price - min_price > max_profit: 
                    max_profit = price - min_price 
            

        return max_profit


        